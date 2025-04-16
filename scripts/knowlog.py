#!/usr/bin/env python3

import rospy
import actionlib
import time

# Replace with the actual import path
from knowrob_ros.msg import TellAction, TellGoal, GraphQueryMessage

class TripleQueryBuilder:
    def __init__(self):
        self.triples = []

    def add(self, subject, predicate, obj):
        """Add a triple to the list."""
        self.triples.append((subject, predicate, obj))

    def build_query_string(self):
        """Generate a Prolog-style query string."""
        return ', '.join(f'{pred}({subj},{obj})' for subj, pred, obj in self.triples)


def feedback_cb(feedback):
    rospy.loginfo("Feedback received: finished=%s", feedback.finished)


def call_tell_action(query_string):
    time.sleep(5)
    rospy.init_node('tell_action_client')

    client = actionlib.SimpleActionClient('/knowrob/tell', TellAction)
    rospy.loginfo("Waiting for action server...")
    client.wait_for_server()
    rospy.loginfo("Connected to action server.")

    # Prepare GraphQueryMessage
    query_msg = GraphQueryMessage()
    query_msg.lang = "LANG_FOL"
    query_msg.queryString = query_string
    query_msg.epistemicOperator = GraphQueryMessage.KNOWLEDGE
    query_msg.temporalOperator = GraphQueryMessage.CURRENTLY
    query_msg.minPastTimestamp = GraphQueryMessage.UNSPECIFIED_TIMESTAMP
    query_msg.maxPastTimestamp = GraphQueryMessage.UNSPECIFIED_TIMESTAMP
    query_msg.confidence = 0.0

    # Wrap in goal and send
    goal = TellGoal(query=query_msg)
    client.send_goal(goal, feedback_cb=feedback_cb)

    rospy.loginfo("Goal sent. Waiting for result...")
    client.wait_for_result()

    result = client.get_result()
    rospy.loginfo("Result received: status=%d", result.status)


if __name__ == "__main__":
    builder = TripleQueryBuilder()
    builder.add("alice", "knows", "bob")
    builder.add("bob", "likes", "pizza")

    query_str = builder.build_query_string()
    rospy.loginfo("Sending query: %s", query_str)

    call_tell_action(query_str)
    print("action called")


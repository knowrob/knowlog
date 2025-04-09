# KnowLog

KnowLog is a package designed to dynamically translate robot plan events into a consistent knowledge graph structure. The knowledge graph adheres to the ABox of the **SOMA ontology**, providing a robust representation of the robot's world and enabling reasoning subsystems to interact with it.

## Overview

The purpose of KnowLog is to facilitate the logging of triples and events from a robot's planning system, and automatically map them to meaningful entities and relations defined in the **SOMA ontology**. This allows the robot's knowledge base to evolve with its actions and reasoning, creating an increasingly rich world model.

## Key Features

- **Event Translation**: KnowLog listens to robot plan events and translates them into semantic triples (subject-predicate-object) that align with the SOMA ontology.
- **Entity Creation**: KnowLog creates new entities in the knowledge graph as needed, ensuring that events and actions are reflected in the context of the robot’s world.
- **Ontology Linkage**: Each event is linked to the correct entities and relations as defined by the SOMA ontology, maintaining the consistency of the knowledge graph.
- **Semantic Enrichment**: Simple properties from events (such as position, speed, or object status) are enriched with semantic meaning by associating them with concepts in the SOMA ontology.
- **Complex Ontological Patterns**: As the robot interacts with the world, KnowLog can generate more complex entities, reflecting more sophisticated relationships and structures inherent in the ontology.

## Installation

To install **KnowLog**, simply clone the repository and install dependencies:

```bash
git clone https://github.com/yourusername/knowlog.git
cd knowlog
pip install -r requirements.txt
```

## Usage
Once installed, you can use KnowLog to start translating your robot's plan events into triples and populate the knowledge graph. Here’s a simple example of how to use the package:

```
from knowlog import KnowLog

# Initialize the KnowLog interface
knowlog = KnowLog()

# Example plan event
event = {
    "action": "move",
    "object": "robot_arm",
    "destination": "shelf_1",
    "properties": {
        "speed": "fast",
        "time": "10s"
    }
}

# Translate the event into a knowledge graph structure
knowlog.translate_event(event)
```

This will translate the event into triples that are stored in a knowledge graph, linking concepts like "robot_arm," "move," and "shelf_1" to their corresponding entities and relationships in the SOMA ontology.

## Contributing
We welcome contributions to **KnowLog**! If you have an idea for an improvement or find a bug, please open an issue or create a pull request.

## License
This project is licensed under the MIT License – see the LICENSE file for details.

## Overview

This repository contains Python implementations of five problems based on search algorithms, pathfinding, and constraint satisfaction techniques. The programs demonstrate shortest-path finding, obstacle avoidance, dynamic path replanning, and map coloring.

## Algorithms Implemented

### 1. Dijkstra's Algorithm – Indian City Routes

* Finds the shortest route between two Indian cities.
* Uses road distances as edge weights.
* Calculates the minimum total travel distance.
* Displays the route and number of visited cities.

### 2. UGV Navigation Using A*

* Simulates an Unmanned Ground Vehicle navigating a 70 × 70 grid.
* Generates obstacles with low, medium, and high density.
* Uses the A* search algorithm with Manhattan distance.
* Finds the shortest available path while avoiding obstacles.
* Visualizes the grid and the calculated path.

### 3. UGV Navigation with Dynamic Obstacles

* Simulates an environment where obstacles can appear during navigation.
* Uses repeated A* search to recalculate the route.
* Allows the UGV to change its path when a new obstacle is detected.
* Measures travel distance and replanning operations.

### 4. Uniform Cost Search – Indian City Routes

* Implements Uniform Cost Search to find a minimum-distance route between Indian cities.
* Uses a priority queue to expand the lowest-cost node.
* Displays the route, total distance, and number of expanded cities.

### 5. Telangana District Map Coloring

* Implements the map coloring problem using backtracking.
* Represents districts as nodes and adjacency relationships as edges.
* Assigns different colors to neighboring districts.
* Uses NetworkX and Matplotlib to visualize the colored graph.

## Technologies Used

* Python
* Matplotlib
* NetworkX
* Heapq
* Random
* Time

## Installation

Install the required libraries using:

```bash
pip install matplotlib networkx
```

## How to Run

1. Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

2. Navigate to the project folder:

```bash
cd AI-Search-Algorithms
```

3. Run the required Python program:

```bash
python filename.py
```

## Evaluation Metrics

The algorithms are evaluated using the following measures:

* Shortest path distance
* Number of nodes explored
* Execution time
* Goal-reaching success
* Number of replanning operations
* Constraint satisfaction in map coloring

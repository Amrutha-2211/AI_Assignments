# Dijkstra's Algorithm – Indian City Shortest Route

## Objective

The objective of this project is to find the shortest route between two Indian cities using Dijkstra's algorithm based on the given road distances.

## Methodology

The following steps are performed:

1. Define the Indian cities and their road distances using an adjacency list.
2. Take the source and destination cities as input.
3. Initialize the distance of the source city as zero and all other cities as infinity.
4. Use a priority queue to select the city with the minimum distance.
5. Update the distances of neighboring cities.
6. Continue until the destination is reached.
7. Reconstruct and display the shortest route.

## Algorithm Used

* Dijkstra's Algorithm

## Result

The program displays:

* Shortest route between the selected cities.
* Total distance of the route in kilometers.
* Number of visited cities.

## Conclusion

The project demonstrates how Dijkstra's algorithm can be used to find the minimum-distance route in a weighted graph. It is useful for understanding shortest-path problems and route optimization.

## Technologies Used

Python
Heapq
Graph Data Structures

## How to Run

Clone the repository and run:

```bash
python dijkstra_indian_cities.py
```

## Sorting Algorithms

In this section, I will be learning about various sorting algorithms. Sorting is a fundamental operation in computer science, and understanding different sorting techniques is crucial for optimizing performance in various applications.

### Bubble Sort
- **Description**: A simple comparison-based sorting algorithm. It repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
- **Time Complexity**: O(n^2)
- **Space Complexity**: O(1)
- **Stability**: Stable

### Selection Sort
- **Description**: An in-place comparison-based sorting algorithm. It divides the input list into two parts: the sorted part at the left end and the unsorted part at the right end. It repeatedly selects the smallest (or largest) element from the unsorted part and moves it to the sorted part.
- **Time Complexity**: O(n^2)
- **Space Complexity**: O(1)
- **Stability**: Not stable

### Insertion Sort
- **Description**: A simple comparison-based sorting algorithm. It builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.
- **Time Complexity**: O(n^2)
- **Space Complexity**: O(1)
- **Stability**: Stable

### Merge Sort
- **Description**: A divide-and-conquer algorithm that divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves.
- **Time Complexity**: O(n log n)
- **Space Complexity**: O(n)
- **Stability**: Stable

### Quick Sort
- **Description**: A divide-and-conquer algorithm. It picks an element as a pivot and partitions the given array around the picked pivot. There are many different versions of quicksort that pick pivot in different ways.
- **Time Complexity**: O(n log n) on average, O(n^2) in the worst case
- **Space Complexity**: O(log n)
- **Stability**: Not stable

### Heap Sort
- **Description**: A comparison-based sorting technique based on a binary heap data structure. It is similar to selection sort where we first find the maximum element and place the maximum element at the end. We repeat the same process for the remaining elements.
- **Time Complexity**: O(n log n)
- **Space Complexity**: O(1)
- **Stability**: Not stable

These sorting algorithms will help me understand different approaches to sorting data and their trade-offs in terms of time and space complexity.
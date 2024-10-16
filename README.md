# ApartmentHunting

This project is designed to assist users in finding the best apartment options while hunting for a place to live. The program allows users to evaluate various apartments based on key criteria such as rent, distance from UCSB, and condition. The primary files involved in this project are:

- **Apartment.py**: Contains the class definition for an Apartment object.
- **lab06.py**: Implements sorting and evaluation functions to analyze apartment data.
- **testFile.py**: Includes test cases to verify the correctness of the implemented functionalities.

## Features

1. **Apartment Class**: 
   - Represents an apartment with attributes for rent, distance from UCSB, and condition (bad, average, excellent).
   - Provides methods to access and display apartment details.

2. **Sorting Functionality**:
   - Implements a merge sort algorithm to sort a list of Apartment objects in ascending order based on the specified criteria.

3. **Evaluation Methods**:
   - `ensureSortedAscending`: Checks if the list of apartments is sorted correctly.
   - `getBestApartment`: Retrieves the apartment with the best overall value.
   - `getWorstApartment`: Retrieves the apartment with the least favorable value.
   - `getAffordableApartments`: Lists all apartments within a specified budget, sorted in ascending order.

## File Descriptions

### Apartment.py
Defines the `Apartment` class with the following attributes and methods:
- **Attributes**:
  - `rent`: Integer representing the apartment's rent.
  - `metersFromUCSB`: Integer representing the distance from UCSB in meters.
  - `condition`: String representing the apartment's condition ("bad", "average", "excellent").
  
- **Methods**:
  - `__init__(self, rent, metersFromUCSB, condition)`: Constructor to initialize the apartment object.
  - `getRent(self)`: Returns the rent of the apartment.
  - `getMetersFromUCSB(self)`: Returns the distance from UCSB.
  - `getCondition(self)`: Returns the condition of the apartment.
  - `getApartmentDetails(self)`: Returns a formatted string with all apartment details.
  - Overloaded comparison operators (`<`, `>`, `==`) to determine the relative quality of apartments.

### ApartmentHunting.py
Contains functions to process a list of Apartment objects:
- `mergesort(apartmentList)`: Sorts the list of apartments using merge sort.
- `ensureSortedAscending(apartmentList)`: Returns a boolean indicating if the list is sorted.
- `getBestApartment(apartmentList)`: Returns details of the best apartment.
- `getWorstApartment(apartmentList)`: Returns details of the worst apartment.
- `getAffordableApartments(apartmentList, budget)`: Returns details of apartments within the specified budget.

### testFile.py
Includes pytest functions that test the functionality of the Apartment class and the sorting/evaluation methods to ensure correctness and reliability.

## Usage
To use this tool, simply create Apartment objects and pass them to the functions in lab06.py to evaluate and sort them based on your preferences.

## Requirements
- Python 3.x
- pytest for testing functionality

from Apartment import Apartment
from lab06 import *

def test_getApartmentDetails():
    a0 = Apartment(1000, 112, "excellent")
    assert a0.getApartmentDetails() == "(Apartment) Rent: $1000, Distance From UCSB: 112m, Condition: excellent"
    a1 = Apartment(981, 200, "average")
    assert a1.getApartmentDetails() == "(Apartment) Rent: $981, Distance From UCSB: 200m, Condition: average"

def test_mergesort():
    a0 = Apartment(500, 215, "bad")
    a1 = Apartment(880, 215, "average")
    a2 = Apartment(1225, 215, "excellent")
    a3 = Apartment(950, 190, "excellent")
    a4 = Apartment(1335, 100, "excellent")
    apartmentList = [a0, a1, a2, a3, a4]
    assert ensureSortedAscending(apartmentList) == False
    mergesort(apartmentList)
    assert ensureSortedAscending(apartmentList) == True

    a0 = Apartment(500, 215, "bad")
    a1 = Apartment(500, 215, "average")
    a2 = Apartment(700, 215, "average")
    a3 = Apartment(700, 215, "excellent")
    apartmentList = [a0, a1, a2, a3]
    assert ensureSortedAscending(apartmentList) == False
    mergesort(apartmentList)
    assert ensureSortedAscending(apartmentList) == True

def test_getBestandWorstApartment():
    a0 = Apartment(1200, 200, "average")
    a1 = Apartment(1300, 200, "excellent")
    a2 = Apartment(1300, 100, "average")
    a3 = Apartment(1000, 215, "excellent")
    a4 = Apartment(1000, 315, "bad")
    apartmentList = [a0, a1, a2, a3, a4]
    assert ensureSortedAscending(apartmentList) == False
    assert getBestApartment(apartmentList) == "(Apartment) Rent: $1000, Distance From UCSB: 215m, Condition: excellent"
    assert getWorstApartment(apartmentList) == "(Apartment) Rent: $1300, Distance From UCSB: 200m, Condition: excellent"

def test_getAffordableApartments():
    a0 = Apartment(800, 205, "excellent")
    a1 = Apartment(900, 205, "average")
    a2 = Apartment(1000, 215, "average")
    a3 = Apartment(1100, 190, "excellent")
    a4 = Apartment(1200, 100, "excellent")
    a5 = Apartment(1300, 100, "bad")
    apartmentList = [a0, a1, a2, a3, a4, a5]
    assert getAffordableApartments(apartmentList, 1200) == ("(Apartment) Rent: $800, Distance From UCSB: 205m, Condition: excellent\n"
                                                            "(Apartment) Rent: $900, Distance From UCSB: 205m, Condition: average\n"
                                                            "(Apartment) Rent: $1000, Distance From UCSB: 215m, Condition: average\n"
                                                            "(Apartment) Rent: $1100, Distance From UCSB: 190m, Condition: excellent\n"
                                                            "(Apartment) Rent: $1200, Distance From UCSB: 100m, Condition: excellent")
    assert getAffordableApartments(apartmentList, 950) == ("(Apartment) Rent: $800, Distance From UCSB: 205m, Condition: excellent\n"
                                                            "(Apartment) Rent: $900, Distance From UCSB: 205m, Condition: average")
    

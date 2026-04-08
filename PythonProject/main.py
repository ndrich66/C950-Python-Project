# Nicole Richards
# ID: 001083248
# Data Structures and Algorithms II — C950
# NHP3 Task 2: WGUPS Routing Program Implementation

# Importing these below inorder for main to function appropriately.
import csv
import datetime

from unicodedata import lookup

import deliveryTruck
from chainingHashTableZyBooks import CreateHashMap
from packages import Packages

# Reading the address CSV file and adding the data to a list, the list will contain the addresses
def load_address_data_table(filename):
    with open(filename) as address_CSV:
        delivery_addresses = csv.reader(address_CSV)
        for address in delivery_addresses:
            address_data_table.append(address[0].strip())

# Create a list to hold address file data.
address_data_table = []

# Load address file data.
load_address_data_table('CVS Files/WGUPS Address Table.csv')

# print operation for testing purposes
# for each_one in address_data_table:
#     print(each_one)

# Reading the distance CSV file and adding the data to a list, the list will contain the distance values.
def load_distance_table(filename):
    with open(filename) as distance_CSV:
        distances = csv.reader(distance_CSV, delimiter=",")
        for distance in distances:
            distance_table_data.append(distance)

# Creating a list to hold distance file data.
distance_table_data = []

# Loading distance file data.
load_distance_table('CVS Files/WGUPS Distance Table.csv')

# test print for distance table
#for row in distance_table_data:
#    print(row)

# Method to gets the address index from the address list.
def get_address_index(address_to_find):
    if address_to_find in address_data_table:
        return address_data_table.index(address_to_find)
    return -1

# Method to determine the distance between two addresses using the distance and address data.
def determine_distance_between_addresses(starting_address, ending_address):
    x_val = get_address_index(starting_address)
    y_val = get_address_index(ending_address)
    distance_delivery = distance_table_data[x_val][y_val]
    if distance_delivery == '':
        distance_delivery = distance_table_data[y_val][x_val]
    return float(distance_delivery)

# Reading the package CSV file and creating a hash table to load said data to.
def package_data_loader(filename, package_hash):
    with open(filename) as package_file:
        packages = csv.reader(package_file)
        for package in packages:
            package_id = int(package[0])
            package_street_address = package[1]
            package_city = package[2]
            package_state = package[3]
            package_zip_code = package[4]
            package_delivery_deadline = package[5]
            package_weight = package[6]
            package_special_notes = package[7]
            package_current_status = "At the hub"
            package_departure_time = None
            package_delivery_time = None
            # The package object.
            package = Packages(package_id, package_street_address, package_city, package_state, package_zip_code,
                               package_delivery_deadline, package_weight, package_special_notes, package_current_status,
                               package_departure_time, package_delivery_time)
            # Print function to test the package object.
            # print(package)

            # Inserts package data into the package hash table.
            package_hash.insert(package_id, package)

# Creating a list to hold package file data.
package_details_file = []
# Creating the hash map for the package data.
package_hash = CreateHashMap()
# Loading the package data into said hash table.
package_data_loader('CVS Files/WGUPS Package Data.csv', package_hash)

# Print function to test package hash table.
# for i in range (len(package_hash.list)):
#     print("key: {} and package: {}".format(i+1, package_hash.lookup(i+1)))

# First truck object.
first_truck = (deliveryTruck.DeliveryTruck
               (1, 0.0, 18, 20, "4001 South 700 East", datetime.timedelta(hours=9, minutes=5),
                [2, 6, 13, 17, 18, 19, 25, 26, 28, 31, 32, 33, 39]))

# Second truck object.
second_truck = (deliveryTruck.DeliveryTruck
                (2, 0.0, 18, 20, "4001 South 700 East", datetime.timedelta(hours=10, minutes=20),
                 [3, 5, 8, 9, 10, 11, 12, 23, 27, 30, 35, 36, 37, 38]))

# Third truck object.
third_truck = (deliveryTruck.DeliveryTruck
               (3,0.0, 18, 20, "4001 South 700 East", datetime.timedelta(hours=8),
                [1, 4, 7, 14, 15, 16, 20, 21, 22, 24, 29, 34, 40]))

# Print functions to test the truck objects.
# print(first_truck)
# print(second_truck)
# print(third_truck)

# Create a method to order the packages on the truck using the nearest neighbor algorithm.
def packages_delivery_service(truck):
    # Create an empty list for undelivered packages.
    yet_to_be_delivered = []
    # Get package ID and append to the list.
    for package_id in truck.package_id:
        package = package_hash.lookup(package_id)
        yet_to_be_delivered.append(package)
    # Empty the list.
    truck.package_id.clear()
    # While loop cycles through not delivered list while their remainders.
    while len(yet_to_be_delivered) > 0:
        ty_next_address = 2000
        for package in yet_to_be_delivered:
            distance_between = determine_distance_between_addresses(truck.current_location, package.street_address)
            # Print function to test address retrival.
            # print(distance_between, ty_next_address)
            if distance_between <= ty_next_address:
                ty_next_address = distance_between
                ty_next_package = package
                # Adds the packages with the nearest address to next package.
                truck.package_id.append(ty_next_package.package_id)
                # Removes said package from the not delivered list
                yet_to_be_delivered.remove(ty_next_package)
                # Adds the miles driven from this package to the miles attribute.
                truck.miles += ty_next_address
                # Updates the trucks current location attribute.
                truck.current_location = ty_next_package.street_address
                # Updates the time taken to get to the address.
                truck.time += datetime.timedelta(hours=ty_next_address/18)
                ty_next_package.delivery_time = truck.time
                ty_next_package.depart_time = truck.depart_time
            else:
                print(" ")
# Loads the packages in the new order on the trucks.
packages_delivery_service(first_truck)
packages_delivery_service(second_truck)
packages_delivery_service(third_truck)

# Create the user interface and main class.
class Main:
    while True:
        print("WESTERN GOVERNORS UNIVERSITY PARCEL SERVICE" )
        print("The total miles for todays deliverys is: ")
        # This prints out total miles for all the packages to be delivered.
        print(first_truck.miles + second_truck.miles + third_truck.miles)
        print("Only enter text prompts exactly as is shown, or the program will terminate. Thank you.")
        # Create prompt for user and gain their input.
        text = input("Please type 'start' to begin. : ")
        if text == "start":
            try:
                # User is prompted to enter a time in hours and minutes.
                user_time = input("Please enter a time to access the status of packages in the HH:MM format or hit enter to exit. : ")
                (hours, minutes) = user_time.split(":")
                convert_timedelta = datetime.timedelta(hours = int(hours), minutes = int(minutes))
                # User is prompted to input if they want to see a single package or all.
                next_user_input = input("To view the status of a specific package please type 'single'. To view the entire list of packages please type 'all'. : ")
                if next_user_input == "single":
                    try:
                        # If single is entered, the user is prompted to enter a package ID number.
                        singular_input_by_user = input("Please enter the package ID number. : ")
                        packages = package_hash.lookup(int(singular_input_by_user))
                        packages.status_update_method(convert_timedelta)
                        print(str(packages))
                        # Exception for error.
                    except ValueError:
                        print("Invalid entry, friend. Terminating program. Goodbye.")
                        exit()
                # If all is entered, a list of all packages will be displayed with the status reflecting the time entered previously.
                elif next_user_input == "all":
                    try:
                        # Lookup function to find package by ID.
                        for package_id in range (1, 41):
                            packages = package_hash.lookup(package_id)
                            packages.status_update_method(convert_timedelta)
                            print(str(packages))
                    # Exception for error.
                    except ValueError:
                        print("Invalid entry, friend. Terminating program. Goodbye.")
                        exit()
                    else:
                        print(" ")
            # Exception for error
            except ValueError:
                        print("Invalid entry, friend. Terminating program. Goodbye.")
                        exit()
        elif input != "start":
            print("Invalid entry, friend. Terminating program. Goodbye.")
            exit()
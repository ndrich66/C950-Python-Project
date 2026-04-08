# Create the class for the delivery truck and attributes.
class DeliveryTruck:

    def __init__ (self, truck_id, miles, speed, capacity, current_location, depart_time, package_id):
        self.truck_id = truck_id
        self.miles = miles
        self.speed = speed
        self.capacity = capacity
        self.current_location = current_location
        self.time = depart_time
        self.depart_time = depart_time
        self.package_id = package_id

    def __str__(self):
        return "%s,%s,%s,%s,%s,%s, %s, %s" % (self.truck_id, self.miles, self.speed, self.capacity, self.current_location,
                                              self.time, self.depart_time, self.package_id)
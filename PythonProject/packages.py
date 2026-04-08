import datetime
# Create the package class and attributes.
class Packages:

    def __init__(self, package_id, street_address, city, state, zip_code, delivery_deadline, weight, special_notes,
             current_status, depart_time, delivery_time):
        self.package_id = package_id
        self.street_address = street_address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.delivery_deadline = delivery_deadline
        self.weight = weight
        self.special_notes = special_notes
        self.current_status = current_status
        self.depart_time = None
        self.delivery_time = None

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (
            self.package_id, self.street_address, self.city, self.state, self.zip_code, self.delivery_deadline,
            self.weight, self.special_notes, self.current_status, self.depart_time, self.delivery_time)
    # This method will update the status of each package at the given time.
    def status_update_method(self, time_input):
        if self.delivery_time is None:
            self.current_status = "At the Hub"
        elif time_input < self.depart_time:
            self.current_status = "At the Hub"
        elif time_input < self.delivery_time:
            self.current_status = "En route"
        else:
            self.current_status = "Delivered"

        # This will change the address for package_id: 9 to the corrected address at the correct time.
        if self.package_id == 9:
            if time_input > datetime.timedelta(hours=10, minutes=20):
                self.street_address = "410 S State St"
                self.zip_code = "84111"
            else:
                self.street_address = "300 State St"
                self.zip_code = "84103"
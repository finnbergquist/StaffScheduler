import csv

class Village(object):

    def __init__(self):
        self.staff = [("Finn Bergquist", 8),("Will Stienfield", 6), ("Rory Sargent", 7),("Seth Turk", 3)] #[("Finn Bergquist", 8),("Will Stienfield", 6)]  list of tuples with name and sessions\
        self.schedule = []


    def addStaffMember(self, name, years):
        """
        :type name: str
        :type years: int
        :rtype: Bool
        """
        if name not in self.staff:#not positive this will work because name is in tuple
            self.staff.append((name, years))
            return True
        else:
            return False

    def importStaff(self):
        with open('staff.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for rows in reader:
                self.addStaffMember(rows[0], int(rows[1]))

    def deleteStaffMember(self, name):
        """
        :type name: str
        :rtype: Bool
        """
        for member in self.staff:
            if member[0] == name:
                self.staff.remove(member)
                return True

        return False


    def setSchedule(self, numDays , peoplePerDay):
        """
        :type numDays: int
        :type peoplePerDay: int
        :rtype: None
        """
        print('hello')
        staff_counter = 0

        for i in range(numDays):
            current_day = []
            for i in range(peoplePerDay):
                current_day.append(self.staff[staff_counter%(len(self.staff))])
                staff_counter+=1

            self.schedule.append(current_day)

        

fro = Village()
fro.importStaff()
print(fro.staff)
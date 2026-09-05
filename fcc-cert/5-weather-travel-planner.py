"""
Travel Weather Planner
-----------------------
Determine whether commuting is possible based on weather, distance,
and vehicle/ride availability.

User Stories:
1. Variables:
   - distance_mi: number, distance to travel in miles
   - is_raining: bool, currently raining or not
   - has_bike: bool, user has a bicycle
   - has_car: bool, user has a car
   - has_ride_share_app: bool, user has a ride-share app

2. Use conditional statements to determine whether commuting is possible.

3. Use if / elif / else to evaluate distance categories in ascending order.

4. If distance_mi is falsy (e.g. 0):
   - print False

5. If distance_mi <= 1 mile:
   - print True only if NOT raining
   - otherwise print False

6. If 1 < distance_mi <= 6 miles:
   - print True only if has_bike AND NOT raining
   - otherwise print False

7. If distance_mi > 6 miles:
   - print True if has_car OR has_ride_share_app
   - otherwise print False
"""

distance_mi = 0
is_raining = True
has_bike = True
has_car = True
has_ride_share_app = True

if not distance_mi:
    print('False')
elif (distance_mi <= 1) and (is_raining == False):
    print('True')
elif (distance_mi > 1 and distance_mi <= 6) and (has_bike == True) and (is_raining == False):
    print('True')
elif (distance_mi > 6) and (has_car == True or has_ride_share_app == True):
    print('True')
else:
    print('False')

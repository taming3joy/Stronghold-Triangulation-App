from math import tan,radians

def convert_gradient(angle):
    angle = -angle
    angle = radians(angle)
    gradient = tan(angle)
    return gradient

def z_coordinate(a,b): #a and b are tuple:(x,z,angle)
    xa,za,angle_a = a
    xb,zb,angle_b = b
    ma,mb = convert_gradient(angle_a),convert_gradient(angle_b)
    z = ((ma*za - mb*zb)+(xb-xa))/(ma-mb)
    return int(z)

def x_coordinate(a,b): #a and b are tuple:(x,z,angle)
    xa,za,angle_a = a
    xb,zb,angle_b = b
    ma,mb = convert_gradient(angle_a),convert_gradient(angle_b)
    x = ((ma*xb-mb*xa)+ma*mb*(za-zb))/(ma-mb)
    return int(x)

def triangulation(a,b):
    return (x_coordinate(a,b),z_coordinate(a,b))

#main
if __name__ == "__main__":
    print("Format: X-coordinate Z-coordinate Angle")
    first_measurement = [float(x) for x in input("Enter 1st measurement: ").split(" ")]
    second_measurement = [float(x) for x in input("Enter 2nd measurement: ").split(" ")]
    stronghold_coordinates_overworld = triangulation(first_measurement,second_measurement)
    stronghold_coordinates_nether = [x//8 for x in stronghold_coordinates_overworld]
    print(f"Overworld: {stronghold_coordinates_overworld}")
    print(f"Nether: {tuple(stronghold_coordinates_nether)}")


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# 1. Define Robot Parameters (Lengths of the arms)
L1 = 5.0
L2 = 4.0
L3 = 6.0

def get_joint_positions(theta1, theta2, theta3):
    # Joint 1 position (elbow)
    x1 = L1 * np.cos(np.deg2rad(theta1))
    y1 = L1 * np.sin(np.deg2rad(theta1))
    
    # Joint 2 position (end-effector / hand)
    x2 = x1 + L2 * np.cos(np.deg2rad(theta1 + theta2))
    y2 = y1 + L2 * np.sin(np.deg2rad(theta1 + theta2))

    x3 = x2 + L3 * np.cos(np.deg2rad(theta1 + theta2 + theta3))
    y3 = y2 + L3 * np.sin(np.deg2rad(theta1 + theta2 + theta3))
    
    return (0, x1, x2, x3), (0, y1, y2, y3)


while True:
    a = int(input("theta1:"))
    b = int(input("theta2:"))
    c = int(input("theta3:"))
    X_coords, Y_coords = get_joint_positions(a, b, c)
    # Plotting
    plt.figure(figsize=(6,6))
    plt.subplots_adjust(bottom=0.25) # Leaves 25% of empty space at the bottom
    plt.plot(X_coords, Y_coords, '-o', linewidth=3, markersize=8, label="Robot Arm")
    #plt.plot(target_x, target_y, 'ro', label="Target (X,Y)")
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    # Format: [Left_X, Bottom_Y, Width, Height]
    slider_position = plt.axes([0.2, 0.1, 0.6, 0.03])
    my_slider = Slider(ax=slider_position, label='Test', valmin=0, valmax=10, valinit=5)

    plt.grid(True)
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.legend()
    plt.title("Robot Arm Inverse Kinematics Simulation")
    plt.show()
# --- TEST THE CODE ---


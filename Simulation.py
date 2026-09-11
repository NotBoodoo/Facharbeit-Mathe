import numpy as np
import matplotlib.pyplot as plt

# 1. Define Robot Parameters (Lengths of the arms)
L1 = 5.0
L2 = 4.0

def get_joint_positions(theta1, theta2):
    # Joint 1 position (elbow)
    x1 = L1 * np.cos(theta1)
    y1 = L1 * np.sin(theta1)
    
    # Joint 2 position (end-effector / hand)
    x2 = x1 + L2 * np.cos(theta1 + theta2)
    y2 = y1 + L2 * np.sin(theta1 + theta2)
    
    return (0, x1, x2), (0, y1, y2)

# --- TEST THE CODE ---


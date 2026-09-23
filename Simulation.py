import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

L1 = 5.0
L2 = 4.0
L3 = 6.0

def get_joint_positions(theta1, theta2, theta3):
    # Joint 1 position (elbow)
    x1 = L1 * np.cos(np.deg2rad(theta1))
    y1 = L1 * np.sin(np.deg2rad(theta1))
    
    # Joint 2 position (wrist)
    x2 = x1 + L2 * np.cos(np.deg2rad(theta1 + theta2))
    y2 = y1 + L2 * np.sin(np.deg2rad(theta1 + theta2))

    # Joint 3 position (end-effector / hand)
    x3 = x2 + L3 * np.cos(np.deg2rad(theta1 + theta2 + theta3))
    y3 = y2 + L3 * np.sin(np.deg2rad(theta1 + theta2 + theta3))
    
    return (0, x1, x2, x3), (0, y1, y2, y3)


# --- SETUP THE GEOMETRIC WINDOW ---
fig, ax = plt.subplots(figsize=(8, 10))
plt.subplots_adjust(bottom=0.25)  

# Axis configurations
ax.set_xlim(-16, 16)
ax.set_ylim(-16, 16)
ax.grid(True)
ax.set_title("Robot Arm Forward Kinematics Simulation")

# --- DRAW INITIAL STATE ---
init_X, init_Y = get_joint_positions(0, 0, 0)

line_reference, = ax.plot(init_X, init_Y, '-o', linewidth=3, markersize=8, label="Robot Arm")
ax.legend()

# --- CREATE TEXT DISPLAY ENGINE FOR COORD INFO ---
# Placing a clean text box in the upper-left inside space of the plot coordinates
# Format: ax.text(X_pos, Y_pos, string_text, box_styling)
text_reference = ax.text(-15, 14, f"Endpunkt:\nX: {init_X[3]:.2f}\nY: {init_Y[3]:.2f}", fontsize=12, fontweight='bold',
                         bbox=dict(facecolor='lightyellow', alpha=0.8, boxstyle='round,pad=0.5'))

# --- CREATE SLIDERS ---
slider_position1 = plt.axes([0.25, 0.15, 0.5, 0.03], facecolor='lightgray')
slider_position2 = plt.axes([0.25, 0.1, 0.5, 0.03], facecolor='lightgray')
slider_position3 = plt.axes([0.25, 0.05, 0.5, 0.03], facecolor='lightgray')

a = Slider(ax=slider_position1, label='Theta1', valmin=-180, valmax=180, valinit=0, valfmt='%1.1f')
b = Slider(ax=slider_position2, label='Theta2', valmin=-170, valmax=170, valinit=0, valfmt='%1.1f')
c = Slider(ax=slider_position3, label='Theta3', valmin=-170, valmax=170, valinit=0, valfmt='%1.1f')


# --- UPDATE LOGIC ---
def update_graph(val):
    a_current = a.val
    b_current = b.val
    c_current = c.val

    # Calculate new math coordinates
    X_coords, Y_coords = get_joint_positions(a_current, b_current, c_current)
    
    # Overwrite the line coordinates mapping data array structure
    line_reference.set_data(X_coords, Y_coords)
    
    # Extract the exact final tip position element index
    tip_x = X_coords[3]
    tip_y = Y_coords[3]
    
    # CRITICAL FIX: Simply rewrite the string property payload values inside the label engine 
    text_reference.set_text(f"Endpunkt:\nX: {tip_x:.2f}\nY: {tip_y:.2f}")
    
    # Redraw the canvas smoothly
    fig.canvas.draw_idle()

# Connect listeners to sliders
a.on_changed(update_graph)
b.on_changed(update_graph)
c.on_changed(update_graph)

plt.show()

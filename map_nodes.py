import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd

img = mpimg.imread("C:\\Users\\Usuario\\Downloads\\NREL118bus.png")
"""
fig, ax = plt.subplots(figsize=(10, 10))
ax.imshow(img)
ax.set_title("Click each node in order (e.g. 1 to 118). Close window when done.")
plt.axis("off")

coords = plt.ginput(n=-1, timeout=0)
plt.close()

df = pd.DataFrame(coords, columns=["x", "y"])
df["node_id"] = range(1, len(df) + 1)

# Reorder columns
df = df[["node_id", "x", "y"]]

# Save to CSV
df.to_csv("node_positions.csv", index=False)

"""
df = pd.read_csv("node_positions.csv")
fig, ax = plt.subplots(figsize=(10, 10))
ax.imshow(img)
ax.scatter(df["x"], df["y"], c="red", s=50, label="Nodes")
for _, row in df.iterrows():
    ax.text(row["x"] + 5, row["y"] + 5, str(int(row["node_id"])),
            color="blue", fontsize=8, weight="bold")
plt.axis("off")
plt.title("Node mapping check — red dots with node numbers")
plt.legend()
plt.show()

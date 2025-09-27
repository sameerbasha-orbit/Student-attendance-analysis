import pandas as pd
import matplotlib.pyplot as plt
import os
from pathlib import Path

# ------------------------------
# Set file paths
# ------------------------------

# Get the folder where this script is located
script_dir = Path(__file__).parent

# Path to the CSV data file
data_path = script_dir.parent / "data" / "attendance.csv"

# Path to save figures
figures_folder = script_dir.parent / "figures"
figures_folder.mkdir(exist_ok=True)  # create folder if it doesn't exist
figure_file = figures_folder / "attendance_plot.png"

# ------------------------------
# Read CSV and clean columns
# ------------------------------

df = pd.read_csv(data_path)
df.columns = df.columns.str.strip()  # remove extra spaces in column names

# ------------------------------
# Calculate attendance percentage
# ------------------------------

df["Attendance_%"] = (df["Attended_Classes"] / df["Total_Classes"]) * 100

# ------------------------------
# Print summaries
# ------------------------------

print("🔹 First 5 Records:")
print(df.head())

print("\n🔹 Average Attendance:")
print(round(df["Attendance_%"].mean(), 2))  # rounded to 2 decimals

# Students below 75% attendance
low_attendance = df[df["Attendance_%"] < 75]
print("\n⚠ Students below 75% attendance:")
print(low_attendance[["StudentID", "Name", "Attendance_%"]])

# Students above or equal 75% attendance
high_attendance = df[df["Attendance_%"] >= 75]
print("\n✅ Students with 75% or above attendance:")
print(high_attendance[["StudentID", "Name", "Attendance_%"]])

# ------------------------------
# Graphical representation
# ------------------------------

plt.figure(figsize=(14,7))
plt.bar(df["Name"], df["Attendance_%"], color="skyblue")
plt.axhline(y=75, color="r", linestyle="--", label="75% Required")
plt.xticks(rotation=90, fontsize=8)
plt.xlabel("Students")
plt.ylabel("Attendance %")
plt.title("Student Attendance Analysis")
plt.legend()

# Save the figure
plt.tight_layout()
plt.savefig(figure_file, dpi=300)
print(f"\n📊 Attendance chart saved at: {figure_file}")

# Optionally display the plot
plt.show()
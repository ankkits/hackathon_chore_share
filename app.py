import pandas as pd
import streamlit as st
import plotly.express as px

# Load data
df = pd.read_csv("chores.csv")

# Compute totals
df["Difference (hrs)"] = df["Average Time (Women, hrs)"] - df["Average Time (Men, hrs)"]
total_women = df["Average Time (Women, hrs)"].sum()
total_men = df["Average Time (Men, hrs)"].sum()

# Bar chart
fig = px.bar(df, x="Chore", y=["Average Time (Women, hrs)", "Average Time (Men, hrs)"],
             barmode='group', title="Time Spent on Household Chores by Gender")

# Streamlit app
st.title("🧹 Chore-Share")

st.markdown(f"#### 🕒 Total Daily Chore Time(based on survey data): \n -The avg time spent by each gender:\n- **Women:** {total_women:.2f} hrs\n- **Men:** {total_men:.2f} hrs\n- **Extra Load on Women:** {total_women - total_men:.2f} hrs")

st.plotly_chart(fig)

st.markdown("### Let’s make chores fun, fair, and gender-balanced!")

st.subheader("🧮 Your Fair Chore Plan")
p1 = st.text_input("Partner 1 Name", "Alice")
p2 = st.text_input("Partner 2 Name", "Bob")
t1 = st.slider(f"{p1}'s Available Time (hrs/day)", 0.0, 5.0, 2.0)
t2 = st.slider(f"{p2}'s Available Time (hrs/day)", 0.0, 5.0, 1.0)

total_available = t1 + t2

st.markdown("#### 📋 Suggested Chore Distribution:")
for _, row in df.iterrows():
    avg_time = (row["Average Time (Women, hrs)"] + row["Average Time (Men, hrs)"]) / 2
    if total_available > 0:
        share1 = avg_time * (t1 / total_available)
        share2 = avg_time * (t2 / total_available)
    else:
        share1 = share2 = 0
    st.write(f"**{row['Chore']}** ➤ {p1}: {share1:.2f} hrs | {p2}: {share2:.2f} hrs")

if t1 < t2:
    st.success(f"💪 {p2} is helping more today – teamwork in action!")
elif t1 > t2:
    st.info(f"🧁 {p1} is pitching in more – maybe {p2} owes a dessert tonight?")
else:
    st.balloons()
    st.success("Perfect balance! You're a chore-sharing dream team!")

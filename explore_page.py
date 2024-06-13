import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def shorted_categories(value_counts, threshold):
    mapping = {}
    for category, counts in value_counts.items():
        if counts >= threshold:
            mapping[category] = category
        else:
            mapping[category] = 'Other'
    return mapping

def Clean_Experience(x):
    if x == 'More than 50 years':
        return 50
    if x == "Less than 1 year":
        return 0.5
    return float(x)

def Clean_Education(x):
    if 'Bachelor’s degree' in x:
        return 'Bachelor’s degree'
    if 'Master’s degree' in x:
        return 'Master’s degree'
    if 'Professional degree' in x or 'Associate degree' in x:
        return 'Post grad'
    else:
        return 'Less than a Bachelors'

@st.cache_data
    
def load_data():
    df = pd.read_csv("Data/survey_results_public.csv")
    df = df[["Country", "EdLevel", "YearsCodePro", "Employment","ConvertedCompYearly"]]
    df = df.rename({"ConvertedCompYearly": "Salary"}, axis=1)
    df = df[df["Salary"].notnull()]
    df = df.dropna()
    df = df[df["Employment"] == "Employed, full-time"]
    df = df.drop("Employment", axis=1)
    country_map = shorted_categories(df.Country.value_counts(), 400)
    df['Country'] = df['Country'].map(country_map)
    df = df[df["Salary"] <= 250000]
    df = df[df["Salary"] >= 10000]
    df = df[df["Country"] != "Other"]
    df["YearsCodePro"] = df['YearsCodePro'].apply(Clean_Experience)
    df["EdLevel"] = df["EdLevel"].apply(Clean_Education)
    
    return df

df = load_data()
def show_explore_page():
    st.title("Explore Software Engineere Salaries")
    
    st.write("""### Stack Overflow Developer Survey 2023""")
    
    data = df["Country"].value_counts()
    
    fig, ax1 = plt.subplots()
    ax1.pie(data, labels = data.index, autopct="%1.1f%%", shadow=True, startangle=90)
    ax1.axis("equal")
    st.write("""### Number of data from different countries""")
    
    st.pyplot(fig)
    
    
    st.write("""### Mean Salary Based On the Country""")
    data = df.groupby(["Country"])["Salary"].mean().sort_values(ascending=True)
    st.bar_chart(data)
    
    st.write("""### Mean Salary Based On the Experience""")
    data = df.groupby(["YearsCodePro"])["Salary"].mean().sort_values(ascending=True)
    st.line_chart(data)
    
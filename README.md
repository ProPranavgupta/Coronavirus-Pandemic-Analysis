# Coronavirus-Pandemic-Analysis

# 🦠 Coronavirus Pandemic Analysis & Interactive Dashboard

An interactive **COVID-19 Pandemic Analysis Dashboard** built with **Python, Pandas, Plotly, and Dash**.
The project analyzes pandemic-related data and presents important statistics through interactive charts, graphs, and state-wise visualizations.

The dashboard allows users to explore **total cases, active cases, recoveries, deaths, medical commodities, and state-wise pandemic data** through an easy-to-use web interface.

---

## 📊 Project Overview

The COVID-19 pandemic generated a huge amount of data related to infections, recoveries, deaths, healthcare resources, and regional impact.

This project converts that data into an **interactive visual dashboard** that helps users understand pandemic trends and compare data across different states.

### Key Information Displayed

* 🦠 Total Cases
* 🏥 Active / Hospitalized Cases
* 💚 Recovered Cases
* ⚠️ Total Deaths
* 🗺️ State-wise Case Distribution
* 😷 Mask Requirements
* 🧴 Sanitizer Requirements
* 🫁 Oxygen Requirements
* 📈 Interactive pandemic trends
* 📊 State-wise comparisons
* 🥧 Interactive distribution charts

---

## ✨ Features

### 📌 Dashboard Statistics

The dashboard displays important pandemic statistics using visual cards:

* Total Cases
* Active Cases
* Recovered Cases
* Total Deaths

### 📊 State-wise Analysis

Users can select different categories and compare pandemic statistics across states.

Available categories:

* All Cases
* Hospitalized
* Recovered
* Deceased

### 📈 Interactive Trend Analysis

The dashboard provides interactive line charts for analyzing:

* Total cases
* Mask requirements
* Sanitizer requirements
* Oxygen requirements

### 🥧 Pandemic Distribution

An interactive pie chart provides a visual representation of selected pandemic categories.

### 🎛️ Interactive Filters

Dropdown menus allow users to dynamically change the data displayed in the charts without reloading the application.

---

## 🛠️ Tech Stack

| Technology         | Purpose                                 |
| ------------------ | --------------------------------------- |
| **Python**         | Core programming language               |
| **Pandas**         | Data loading and analysis               |
| **Plotly**         | Interactive data visualization          |
| **Plotly Express** | Simplified visualization                |
| **Dash**           | Interactive web dashboard               |
| **Bootstrap 5**    | Dashboard styling and responsive layout |

---

## 📁 Project Structure

```text
Coronavirus-Pandemic-Analysis/
│
├── app.py
├── state_wise_daily data file.csv
├── README.md
└── requirements.txt
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/coronavirus-pandemic-analysis.git
```

### 2. Navigate to the project directory

```bash
cd coronavirus-pandemic-analysis
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
python app.py
```

The dashboard will be available at:

```text
http://127.0.0.1:8050/
```

---

## 📦 Requirements

Create a `requirements.txt` file containing:

```text
pandas
plotly
dash
```

---

## 🖥️ Dashboard Workflow

```text
COVID-19 Dataset
       │
       ▼
   Pandas
(Data Processing)
       │
       ▼
   Dash + Plotly
(Interactive Charts)
       │
       ▼
Interactive Dashboard
       │
       ├── Total Cases
       ├── Active Cases
       ├── Recoveries
       ├── Deaths
       ├── State-wise Analysis
       ├── Medical Commodities
       └── Distribution Analysis
```

---

## 📈 Data Analysis

The application reads pandemic data from a CSV file using Pandas.

```python
patients = pd.read_csv('state_wise_daily data file.csv')
```

The dataset is then used to calculate and visualize different pandemic statistics.

For example:

```python
total = patients.shape[0]

active = patients[
    patients['Status'] == 'Confirmed'
].shape[0]

recovered = patients[
    patients['Status'] == 'Recovered'
].shape[0]

deaths = patients[
    patients['Status'] == 'Deceased'
].shape[0]
```

These values are displayed on the dashboard as summary statistics.

---

## 📊 Visualizations

The project uses different visualization techniques for different types of analysis.

### Bar Chart

Used for comparing pandemic statistics across states.

### Line Chart

Used for displaying trends in:

* Total cases
* Masks
* Sanitizers
* Oxygen

### Donut / Pie Chart

Used to show the distribution of selected categories.

---

## 🎯 Project Objectives

The main objectives of this project are:

1. Analyze COVID-19 pandemic data.
2. Create an interactive data visualization dashboard.
3. Compare pandemic statistics across different states.
4. Visualize healthcare commodity requirements.
5. Make complex pandemic data easier to understand.
6. Practice real-world data analysis using Python.

---
## ⚠️ Disclaimer

This project is created for **educational and data visualization purposes**.

The analysis and visualizations depend on the dataset provided with the project. The displayed results should not be considered as official medical or epidemiological statistics.

---

## 👨‍💻 Author

**Pranav Gupta**

Computer Science Student | AI & Machine Learning Enthusiast

Interested in:

* Artificial Intelligence
* Machine Learning
* Generative AI
* Data Science
* Python
* Software Development

---

## ⭐ Support

If you found this project useful or interesting, consider giving the repository a ⭐ on GitHub.

---

## 📜 License

This project is available for educational and personal use.

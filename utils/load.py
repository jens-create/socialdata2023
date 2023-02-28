# load SF data!
import pandas as pd


def load_sf():
    df = pd.read_csv(
        "/Users/jenspt/Desktop/git/socialdata2023/assignments/data/"
        + "Police_Department_Incident_Reports__Historical_2003_to_May_2018.csv"
    )
    df["Timestamp"] = pd.to_datetime(df["Date"] + df["Time"], format="%m/%d/%Y%H:%M")
    df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%Y")
    df = df[df["Timestamp"] < "12/31/2017"]
    df["hour"] = df["Timestamp"].dt.hour
    df["minute"] = df["Timestamp"].dt.minute
    df["hod"] = df["Timestamp"].dt.hour + df["Timestamp"].dt.minute / 60
    df["year"] = df["Timestamp"].dt.year
    df["month"] = df["Timestamp"].dt.month
    df["dow"] = df["Timestamp"].dt.dayofweek
    df["how"] = df["Timestamp"].dt.dayofweek * 24 + df["Timestamp"].dt.hour
    return df

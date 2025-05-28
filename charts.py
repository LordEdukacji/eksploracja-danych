import inspect
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numericize import *

def age_hist(df):
    plt.clf()

    plt.hist(df.Age, bins=[18,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100])

    plt.ylabel("Liczba próbek")
    plt.title("Histogram atrybutu Age")

    plt.savefig("hist/" + inspect.stack()[0][3] + ".png", bbox_inches='tight')

    def limit_age(row):
        if row["Age"] < 18 or row["Age"] > 100:
            return None
        else:
            return  row["Age"]
        
    df["_age"] = df.apply(limit_age, axis=1)

def gender_hist(df):
    plt.clf()

    male_terms = ["Male",
    "male",
    "M",
    "m",
    "Make",
    "Male",
    "Cis Male",
    "Man",
    "Mal",
    "Male (CIS)",
    "msle",
    "cis male",
    "Mail",
    "Cis Man",
    "maile"]

    female_terms = ["Female",
    "female",
    "F",
    "f",
    "Woman",
    "Female",
    "Female (cis)",
    "cis-female/femme",
    "Malr",
    "femail",
    "Cis Female",
    "Femake",
    "woman"
    ]

    rejected_terms = ["Nah", "All", "ostensibly male, unsure what that really means", "p", "Neuter", "A little about you"]

    def normalize_gender(row):
        if row["Gender"] in male_terms:
            return "Male"
        elif row["Gender"] in female_terms:
            return "Female"
        elif row["Gender"] in rejected_terms:
            return None
        else:
            return "Other"

    df["gender_normalized"] = df.apply(normalize_gender, axis=1)

    pd.Series(df.gender_normalized).value_counts(sort=False).plot(kind='bar')

    plt.ylabel("Liczba próbek")
    plt.title("Histogram znormalizowanego atrybutu Gender")

    plt.savefig("hist/" + inspect.stack()[0][3] + ".png", bbox_inches='tight')

    df["_gender"] = df.apply(numericize_gender, axis=1)

def country_hist(df):
    plt.clf()

    plt.hist(df.Country, bins = df.Country.unique())
    plt.xticks(rotation=90)

    plt.ylabel("Liczba próbek")
    plt.title("Histogram atrybutu Country")

    plt.savefig("hist/" + inspect.stack()[0][3] + ".png", bbox_inches='tight')

def state_hist(df):
    plt.clf()

    pd.Series(df.state).value_counts(sort=False).plot(kind='bar')

    plt.ylabel("Liczba próbek")
    plt.title("Histogram atrybutu state")

    plt.savefig("hist/" + inspect.stack()[0][3] + ".png", bbox_inches='tight')

def self_employed_hist(df):
    plt.clf()

    pd.Series(df.self_employed).value_counts(sort=False).plot(kind='bar')

    plt.ylabel("Liczba próbek")
    plt.title("Histogram atrybutu self_employed")

    plt.savefig("hist/" + inspect.stack()[0][3] + ".png", bbox_inches='tight')

    df["_self_employed"] = df.apply(numericize_yes_no, attribute="self_employed", axis=1)

def family_history_hist(df):
    plt.clf()

    pd.Series(df.family_history).value_counts(sort=False).plot(kind='bar')

    plt.ylabel("Liczba próbek")
    plt.title("Histogram atrybutu family_history")

    plt.savefig("hist/" + inspect.stack()[0][3] + ".png", bbox_inches='tight')

    df["_family_history"] = df.apply(numericize_yes_no, attribute="family_history", axis=1)

def treatment_hist(df):
    plt.clf()

    pd.Series(df.treatment).value_counts(sort=False).plot(kind='bar')

    plt.ylabel("Liczba próbek")
    plt.title("Histogram atrybutu treatment")

    plt.savefig("hist/" + inspect.stack()[0][3] + ".png", bbox_inches='tight')

    df["_treatment"] = df.apply(numericize_yes_no, attribute="treatment", axis=1)

def work_interfere_hist(df):
    plt.clf()

    pd.Series(df.work_interfere).value_counts(sort=False).plot(kind='bar')

    plt.ylabel("Liczba próbek")
    plt.title("Histogram atrybutu work_interfere")

    plt.savefig("hist/" + inspect.stack()[0][3] + ".png", bbox_inches='tight')

    df["_work_interfere"] = df.apply(numericize_frequency, attribute="work_interfere", axis=1)

def no_employees_hist(df):
    plt.clf()

    pd.Series(df.no_employees).value_counts(sort=False).plot(kind='bar')

    plt.ylabel("Liczba próbek")
    plt.title("Histogram atrybutu no_employees")

    plt.savefig("hist/" + inspect.stack()[0][3] + ".png", bbox_inches='tight')

    df["_no_employees"] = df.apply(numericize_no_employees, attribute="no_employees", axis=1)

def remote_work_hist(df):
    plt.clf()

    pd.Series(df.remote_work).value_counts(sort=False).plot(kind='bar')

    plt.ylabel("Liczba próbek")
    plt.title("Histogram atrybutu remote_work")

    plt.savefig("hist/" + inspect.stack()[0][3] + ".png", bbox_inches='tight')

    df["_remote_work"] = df.apply(numericize_yes_no, attribute="remote_work", axis=1)

def tech_company_hist(df):
    plt.clf()

    pd.Series(df.tech_company).value_counts(sort=False).plot(kind='bar')

    plt.ylabel("Liczba próbek")
    plt.title("Histogram atrybutu tech_company")

    plt.savefig("hist/" + inspect.stack()[0][3] + ".png", bbox_inches='tight')

    df["_tech_company"] = df.apply(numericize_yes_no, attribute="tech_company", axis=1)

def benefits_hist(df):
    plt.clf()

    pd.Series(df.benefits).value_counts(sort=False).plot(kind='bar')

    plt.ylabel("Liczba próbek")
    plt.title("Histogram atrybutu benefits")

    plt.savefig("hist/" + inspect.stack()[0][3] + ".png", bbox_inches='tight')

    df["_benefits"] = df.apply(numericize_yes_no, attribute="benefits", axis=1)

def care_options_hist(df):
    plt.clf()

    pd.Series(df.care_options).value_counts(sort=False).plot(kind='bar')

    plt.ylabel("Liczba próbek")
    plt.title("Histogram atrybutu care_options")

    plt.savefig("hist/" + inspect.stack()[0][3] + ".png", bbox_inches='tight')

    df["_care_options"] = df.apply(numericize_yes_no, attribute="care_options", axis=1)

def wellness_program_hist(df):
    plt.clf()

    pd.Series(df.wellness_program).value_counts(sort=False).plot(kind='bar')

    plt.ylabel("Liczba próbek")
    plt.title("Histogram atrybutu wellness_program")

    plt.savefig("hist/" + inspect.stack()[0][3] + ".png", bbox_inches='tight')

    df["_wellness_program"] = df.apply(numericize_yes_no, attribute="wellness_program", axis=1)

def seek_help_hist(df):
    plt.clf()

    pd.Series(df.seek_help).value_counts(sort=False).plot(kind='bar')

    plt.ylabel("Liczba próbek")
    plt.title("Histogram atrybutu seek_help")

    plt.savefig("hist/" + inspect.stack()[0][3] + ".png", bbox_inches='tight')
    
    df["_seek_help"] = df.apply(numericize_yes_no, attribute="seek_help", axis=1)

def anonymity_hist(df):
    plt.clf()

    pd.Series(df.anonymity).value_counts(sort=False).plot(kind='bar')

    plt.ylabel("Liczba próbek")
    plt.title("Histogram atrybutu anonymity")

    plt.savefig("hist/" + inspect.stack()[0][3] + ".png", bbox_inches='tight')

    df["_anonymity"] = df.apply(numericize_yes_no, attribute="anonymity", axis=1)

def leave_hist(df):
    plt.clf()

    pd.Series(df.leave).value_counts(sort=False).plot(kind='bar')

    plt.ylabel("Liczba próbek")
    plt.title("Histogram atrybutu leave")

    plt.savefig("hist/" + inspect.stack()[0][3] + ".png", bbox_inches='tight')

    df["_leave"] = df.apply(numericize_difficulty, attribute="leave", axis=1)

def mental_health_consequence_hist(df):
    plt.clf()

    pd.Series(df.mental_health_consequence).value_counts(sort=False).plot(kind='bar')

    plt.ylabel("Liczba próbek")
    plt.title("Histogram atrybutu mental_health_consequence")

    plt.savefig("hist/" + inspect.stack()[0][3] + ".png", bbox_inches='tight')

    df["_mental_health_consequence"] = df.apply(numericize_yes_no, attribute="mental_health_consequence", axis=1)

def phys_health_consequence_hist(df):
    plt.clf()

    pd.Series(df.phys_health_consequence).value_counts(sort=False).plot(kind='bar')

    plt.ylabel("Liczba próbek")
    plt.title("Histogram atrybutu phys_health_consequence")

    plt.savefig("hist/" + inspect.stack()[0][3] + ".png", bbox_inches='tight')

    df["_phys_health_consequence"] = df.apply(numericize_yes_no, attribute="phys_health_consequence", axis=1)

def coworkers_hist(df):
    plt.clf()

    pd.Series(df.coworkers).value_counts(sort=False).plot(kind='bar')

    plt.ylabel("Liczba próbek")
    plt.title("Histogram atrybutu coworkers")

    plt.savefig("hist/" + inspect.stack()[0][3] + ".png", bbox_inches='tight')

    df["_coworkers"] = df.apply(numericize_yes_no, attribute="coworkers", axis=1)

def supervisor_hist(df):
    plt.clf()

    pd.Series(df.supervisor).value_counts(sort=False).plot(kind='bar')

    plt.ylabel("Liczba próbek")
    plt.title("Histogram atrybutu supervisor")

    plt.savefig("hist/" + inspect.stack()[0][3] + ".png", bbox_inches='tight')

    df["_supervisor"] = df.apply(numericize_yes_no, attribute="supervisor", axis=1)

def mental_health_interview_hist(df):
    plt.clf()

    pd.Series(df.mental_health_interview).value_counts(sort=False).plot(kind='bar')

    plt.ylabel("Liczba próbek")
    plt.title("Histogram atrybutu mental_health_interview")

    plt.savefig("hist/" + inspect.stack()[0][3] + ".png", bbox_inches='tight')

    df["_mental_health_interview"] = df.apply(numericize_yes_no, attribute="mental_health_interview", axis=1)

def phys_health_interview_hist(df):
    plt.clf()

    pd.Series(df.phys_health_interview).value_counts(sort=False).plot(kind='bar')

    plt.ylabel("Liczba próbek")
    plt.title("Histogram atrybutu phys_health_interview")

    plt.savefig("hist/" + inspect.stack()[0][3] + ".png", bbox_inches='tight')

    df["_phys_health_interview"] = df.apply(numericize_yes_no, attribute="phys_health_interview", axis=1)

def mental_vs_physical_hist(df):
    plt.clf()

    pd.Series(df.mental_vs_physical).value_counts(sort=False).plot(kind='bar')

    plt.ylabel("Liczba próbek")
    plt.title("Histogram atrybutu mental_vs_physical")

    plt.savefig("hist/" + inspect.stack()[0][3] + ".png", bbox_inches='tight')

    df["_mental_vs_physical"] = df.apply(numericize_yes_no, attribute="mental_vs_physical", axis=1)

def obs_consequence_hist(df):
    plt.clf()

    pd.Series(df.obs_consequence).value_counts(sort=False).plot(kind='bar')

    plt.ylabel("Liczba próbek")
    plt.title("Histogram atrybutu obs_consequence")

    plt.savefig("hist/" + inspect.stack()[0][3] + ".png", bbox_inches='tight')

    df["_obs_consequence"] = df.apply(numericize_yes_no, attribute="obs_consequence", axis=1)
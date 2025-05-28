import inspect
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def age_hist(df):
    plt.clf()

    plt.hist(df.Age, bins=[18,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100])

    plt.ylabel("Liczba próbek")
    plt.title("Histogram atrybutu Age")

    plt.savefig("hist/" + inspect.stack()[0][3] + ".png", bbox_inches='tight')

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

def family_history_hist(df):
    plt.clf()

    pd.Series(df.family_history).value_counts(sort=False).plot(kind='bar')

    plt.ylabel("Liczba próbek")
    plt.title("Histogram atrybutu family_history")

    plt.savefig("hist/" + inspect.stack()[0][3] + ".png", bbox_inches='tight')

def treatment_hist(df):
    plt.clf()

    pd.Series(df.treatment).value_counts(sort=False).plot(kind='bar')

    plt.ylabel("Liczba próbek")
    plt.title("Histogram atrybutu treatment")

    plt.savefig("hist/" + inspect.stack()[0][3] + ".png", bbox_inches='tight')

def work_interfere_hist(df):
    plt.clf()

    pd.Series(df.work_interfere).value_counts(sort=False).plot(kind='bar')

    plt.ylabel("Liczba próbek")
    plt.title("Histogram atrybutu work_interfere")

    plt.savefig("hist/" + inspect.stack()[0][3] + ".png", bbox_inches='tight')

def no_employees_hist(df):
    plt.clf()

    pd.Series(df.no_employees).value_counts(sort=False).plot(kind='bar')

    plt.ylabel("Liczba próbek")
    plt.title("Histogram atrybutu no_employees")

    plt.savefig("hist/" + inspect.stack()[0][3] + ".png", bbox_inches='tight')

def remote_work_hist(df):
    plt.clf()

    pd.Series(df.remote_work).value_counts(sort=False).plot(kind='bar')

    plt.ylabel("Liczba próbek")
    plt.title("Histogram atrybutu remote_work")

    plt.savefig("hist/" + inspect.stack()[0][3] + ".png", bbox_inches='tight')

def tech_company_hist(df):
    plt.clf()

    pd.Series(df.tech_company).value_counts(sort=False).plot(kind='bar')

    plt.ylabel("Liczba próbek")
    plt.title("Histogram atrybutu tech_company")

    plt.savefig("hist/" + inspect.stack()[0][3] + ".png", bbox_inches='tight')

def benefits_hist(df):
    plt.clf()

    pd.Series(df.benefits).value_counts(sort=False).plot(kind='bar')

    plt.ylabel("Liczba próbek")
    plt.title("Histogram atrybutu benefits")

    plt.savefig("hist/" + inspect.stack()[0][3] + ".png", bbox_inches='tight')

def care_options_hist(df):
    plt.clf()

    pd.Series(df.care_options).value_counts(sort=False).plot(kind='bar')

    plt.ylabel("Liczba próbek")
    plt.title("Histogram atrybutu care_options")

    plt.savefig("hist/" + inspect.stack()[0][3] + ".png", bbox_inches='tight')

def wellness_program_hist(df):
    plt.clf()

    pd.Series(df.wellness_program).value_counts(sort=False).plot(kind='bar')

    plt.ylabel("Liczba próbek")
    plt.title("Histogram atrybutu wellness_program")

    plt.savefig("hist/" + inspect.stack()[0][3] + ".png", bbox_inches='tight')

def seek_help_hist(df):
    plt.clf()

    pd.Series(df.seek_help).value_counts(sort=False).plot(kind='bar')

    plt.ylabel("Liczba próbek")
    plt.title("Histogram atrybutu seek_help")

    plt.savefig("hist/" + inspect.stack()[0][3] + ".png", bbox_inches='tight')

def anonymity_hist(df):
    plt.clf()

    pd.Series(df.anonymity).value_counts(sort=False).plot(kind='bar')

    plt.ylabel("Liczba próbek")
    plt.title("Histogram atrybutu anonymity")

    plt.savefig("hist/" + inspect.stack()[0][3] + ".png", bbox_inches='tight')

def leave_hist(df):
    plt.clf()

    pd.Series(df.leave).value_counts(sort=False).plot(kind='bar')

    plt.ylabel("Liczba próbek")
    plt.title("Histogram atrybutu leave")

    plt.savefig("hist/" + inspect.stack()[0][3] + ".png", bbox_inches='tight')

def mental_health_consequence_hist(df):
    plt.clf()

    pd.Series(df.mental_health_consequence).value_counts(sort=False).plot(kind='bar')

    plt.ylabel("Liczba próbek")
    plt.title("Histogram atrybutu mental_health_consequence")

    plt.savefig("hist/" + inspect.stack()[0][3] + ".png", bbox_inches='tight')

def phys_health_consequence_hist(df):
    plt.clf()

    pd.Series(df.phys_health_consequence).value_counts(sort=False).plot(kind='bar')

    plt.ylabel("Liczba próbek")
    plt.title("Histogram atrybutu phys_health_consequence")

    plt.savefig("hist/" + inspect.stack()[0][3] + ".png", bbox_inches='tight')

def coworkers_hist(df):
    plt.clf()

    pd.Series(df.coworkers).value_counts(sort=False).plot(kind='bar')

    plt.ylabel("Liczba próbek")
    plt.title("Histogram atrybutu coworkers")

    plt.savefig("hist/" + inspect.stack()[0][3] + ".png", bbox_inches='tight')

def supervisor_hist(df):
    plt.clf()

    pd.Series(df.supervisor).value_counts(sort=False).plot(kind='bar')

    plt.ylabel("Liczba próbek")
    plt.title("Histogram atrybutu supervisor")

    plt.savefig("hist/" + inspect.stack()[0][3] + ".png", bbox_inches='tight')

def mental_health_interview_hist(df):
    plt.clf()

    pd.Series(df.mental_health_interview).value_counts(sort=False).plot(kind='bar')

    plt.ylabel("Liczba próbek")
    plt.title("Histogram atrybutu mental_health_interview")

    plt.savefig("hist/" + inspect.stack()[0][3] + ".png", bbox_inches='tight')

def phys_health_interview_hist(df):
    plt.clf()

    pd.Series(df.phys_health_interview).value_counts(sort=False).plot(kind='bar')

    plt.ylabel("Liczba próbek")
    plt.title("Histogram atrybutu phys_health_interview")

    plt.savefig("hist/" + inspect.stack()[0][3] + ".png", bbox_inches='tight')

def mental_vs_physical_hist(df):
    plt.clf()

    pd.Series(df.mental_vs_physical).value_counts(sort=False).plot(kind='bar')

    plt.ylabel("Liczba próbek")
    plt.title("Histogram atrybutu mental_vs_physical")

    plt.savefig("hist/" + inspect.stack()[0][3] + ".png", bbox_inches='tight')

def obs_consequence_hist(df):
    plt.clf()

    pd.Series(df.obs_consequence).value_counts(sort=False).plot(kind='bar')

    plt.ylabel("Liczba próbek")
    plt.title("Histogram atrybutu obs_consequence")

    plt.savefig("hist/" + inspect.stack()[0][3] + ".png", bbox_inches='tight')
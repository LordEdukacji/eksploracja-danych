import pandas as pd
import charts

def main():
    df = pd.read_csv("survey.csv")

    charts.age_hist(df)
    charts.gender_hist(df)
    charts.country_hist(df)
    charts.state_hist(df)
    charts.self_employed_hist(df)
    charts.family_history_hist(df)
    charts.treatment_hist(df)
    charts.work_interfere_hist(df)
    charts.no_employees_hist(df)
    charts.remote_work_hist(df)
    charts.tech_company_hist(df)
    charts.benefits_hist(df)
    charts.care_options_hist(df)
    charts.wellness_program_hist(df)
    charts.seek_help_hist(df)
    charts.anonymity_hist(df)
    charts.leave_hist(df)
    charts.mental_health_consequence_hist(df)
    charts.phys_health_consequence_hist(df)
    charts.coworkers_hist(df)
    charts.supervisor_hist(df)
    charts.mental_health_interview_hist(df)
    charts.phys_health_interview_hist(df)
    charts.mental_vs_physical_hist(df)
    charts.obs_consequence_hist(df)

if __name__ == "__main__":
    main()
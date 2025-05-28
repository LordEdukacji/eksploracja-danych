import pandas as pd
import charts
import matplotlib.pyplot as plt
import seaborn as sns

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

    df2 = df[[ "_age",
               "_gender",
               "_self_employed",
               "_family_history",
               "_treatment",
               "_work_interfere",
               "_no_employees",
               "_remote_work",
               "_tech_company",
               "_benefits",
               "_care_options",
               "_wellness_program",
               "_seek_help",
               "_anonymity",
               "_leave",
               "_mental_health_consequence",
               "_phys_health_consequence",
               "_coworkers",
               "_supervisor",
               "_mental_health_interview",
               "_phys_health_interview",
               "_mental_vs_physical",
               "_obs_consequence"
               ]]
    
    """ co = df2.corr(method="pearson")
    plt.clf()
    sns.heatmap(co)
    plt.title("Macierz korelacji metodą Pearsona")
    plt.savefig("heatmap.png", bbox_inches='tight') """
    
    print(df2.corr(method="pearson"))

    co2 = df2.corrwith(df2["_treatment"])
    plt.clf()
    plt.barh(df2.columns, co2)
    plt.title("Korelacja metodą Pearsona według atrybutu treatment")
    plt.savefig("corr.png", bbox_inches='tight')
    

if __name__ == "__main__":
    main()
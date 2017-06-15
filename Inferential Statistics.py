# import custom modules wrote by julio
import seaborn as sns
import pandas as pd
%matplotlib inline
#from capstone_01 import clean_data
from ispy1 import inferential_statistics

# reload modules without restartign the kernel (makes development easier)
# import importlib
#importlib.reload(inferential_statistics);

df = pd.read_csv('./data/I-SPY_1_clean_data.csv')
df.head(2)

predictor= ['age']
outcome = 'Alive'
anova_table, OLS = inferential_statistics.linear_models(df, outcome, predictor);
sns.boxplot(x= outcome, y=predictor[0], data=df, palette="Set3");

# create a boxplot to visualize this interaction
ax = sns.boxplot(x= 'PCR', y='age', hue ='Alive',data=df, palette="Set3");
ax.set_title('Interactions between age, survival, and PCR');

predictors = ['PCR']
outcome = 'Alive'
inferential_statistics.categorical_data(outcome, predictors, df)
inferential_statistics.contingency_table('PCR', 'Alive',df)






### Interaction PCR, AGE and `PCR`
# create a boxplot to visualize this interaction
ax = sns.boxplot(x= 'PCR', y='age', hue ='Alive',data=df, palette="Set3");
ax.set_title('Interactions between age, survival, and PCR');
plt.show()

# orgnize data to peform anova on 

# create dataframe only for patients with PCR = Yes
Patients_with_PCR = df.loc[df.PCR=='Yes',:]

# ANOVA for Alive vs Age for PCR = Yes Only 
# create dataframe only for patients with PCR = Yes
df_by_PCR = df.loc[df.PCR=='No',:]
df_by_PCR.head()

# Anova age vs Alive
predictor= ['age']
outcome = 'Alive'
anova_table, OLS = inferential_statistics.linear_models(df_by_PCR, outcome, predictor);

R = inferential_statistics.anova_MRI('PCR', df);


mri_features = ['MRI_LD_Baseline', 'MRI_LD_1_3dAC', 'MRI_LD_Int_Reg', 'MRI_LD_PreSurg']
outcome = 'Alive'
# Effect Size
inferential_statistics.effect_size( df, mri_features, outcome)


outcome = 'Alive'
R = inferential_statistics.anova_MRI(outcome, df);

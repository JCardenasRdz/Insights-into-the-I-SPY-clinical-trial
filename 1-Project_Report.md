# Insights into the I-SPY clinical trial
#### by Julio Cardenas-Rodriguez (@jdatascientist)

## 1. Description and Objectives
The goal of this project is to improve the prediction of clinical outcomes to neoadjuvant chemotherapy in patients with breast cancer. Currently, most patients with breast cancer undergo neoadjuvant chemotherapy, which is aimed at reducing the size of a tumor (burden) before surgery to remove the tumor or the entire breast.   
Some of the patients response completely to the therapy and the patient does not present any residual tumor at the time of surgery (Pathologic complete response or `PCR`). On the other hand, most patients have residual disease at the time of surgery and further treatment or surgery is required.

## 2. Data source
All data for the **222 patients** treated for breast cancer in the IPSY-1 clinical trial was obtained from the [cancer imaging archive](https://wiki.cancerimagingarchive.net/display/Public/ISPY1) and the Breast Imaging Research Program at UCSF. To facilitate the dissemination and reproducibility of this analysis, the raw data and all code were posted at [Data.World](https://data.world/julio/ispy-1-trial) and [Github](https://github.com/JCardenasRdz/Insights-into-the-I-SPY-clinical-trial) and are available under an MIT license.

## 3. Source code in Python and data analysis
The code is organized in a Python package (`ispy1`), with modules for each of the four steps of the data analysis

> - ispy1
>   - clean_data.py
>   - inferential_statistics.py
>   - predictive_statistics.py
>   - survival_analysis.py

## 4. Description of the data
> The data contained in the cancer imaging archive is organized column-wise for all subjects as follows (rows = patients).

**Clinical Outcomes**
1. Survival Status at the end of the study (`Survival`):
    - 7 = Alive
    - 8 = Dead
    - 9 = Lost to follow up
2. Length of Survival (`Survival_length`):
    - Days from study entry to death or last follow-up
3. Recurrence-free survival (`RFS`):
    - days from from NCAC start until progression or death
4. Recurrence-free survival indicator (`RFS_code`)
    - progression or death (1),
    - removed from survival curve (0)
5. Pathologic Complete Response (`PCR`) post-neoadjuvant ?:
    - 1 = Yes
    - 0 = No
    - Lost (Blank)
6. Residual Cancer Burden class (`RCB`):
    - 0 = RCB index (Class 0)
    - 1 = RCB index less than or equal to 1.36 (Class I)
    - 2 = RCB index greater than 1.36 or equal to 3.28  (Class II)
    - 3 = III, RCB index greater than 3.28 (Class III)
    - Blank = unavailable or no surgery

**Predictors of clinical outcomes**
1. `Age` (Years)
2. `Race`, encoded as:
    - 1 = Caucasian
    - 3 = African American
    - 4 = Asian
    - 5 = Native Hawaiian
    - 6 = American Indian
    - 50 = Multiple race
3. Estrogen Receptor Status (`ER+`) encoded as:
    - 1 = Positive
    - 0 = Negative
    - Blank = Indeterminate
4. Progesterone Receptor Status (`PR+`) encoded as:
    - 1 = Positive
    - 0 = Negative
    - Blank = Indeterminate
5. Hormone Receptor Status (`ER+`)
    - 1 = Positive
    - 0 = Negative
    - Blank = Indeterminate
6. Bilateral Breast Cancer (`Bilateral`):
    - 1 = Cancer Detected on both breasts
    - 0 = Cancer Detected in a single breast
7. Breast with major or single Tumor (`Laterality`):
    - 1 = Left breast
    - 2 = Right breast
8. Largest tumor dimension at Baseline estimated by MRI (`MRI_LD_Baseline`, continous variable)
9. Largest tumor dimension 1-3 days after NAC estimated by MRI (`MRI_LD_1_3dAC`, continous variable)
10. Largest tumor dimension between cycles of NAC estimated by MRI (`MRI_LD_Int_Reg`, continous variable)
11. Largest tumor dimension before surgery estimated by MRI (`MRI_LD_PreSurg`, continous variable)

## Data cleaning and organizing
The data for this study was provided as an excel file (.xls) with multiple fields and is not suitable to construct the contingency tables required for inferential statistics or to peform predictive statistics using `sklearn` and `statsmodels`. The module `clean_data` of the `ipsy1` was used to clean the data and generate a pandas dataframe. T he code for  `clean_data` module can be found [here](https://gist.github.com/JCardenasRdz/75dd152afe6250a5c7de2315b2a2a960).  

```Python
# load module by Julio and pandas
from ispy1 import clean_data
import pandas as pd

file = './data/I-SPY_1_All_Patient_Clinical_and_Outcome_Data.xlsx'
df = clean_data.clean_my_data(file)
df.head(2)

# save clean data in new  csv file
df.to_csv('./data/I-SPY_1_clean_data.csv')
df.head(2)
```
![df](./images/1.png)



  The analysis for this data set was divided in three phases: _1) Cleaning and organizing,

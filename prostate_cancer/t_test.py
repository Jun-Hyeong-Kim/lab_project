import pandas as pd
from scipy import stats

# Load the data into a Pandas DataFrame
df = pd.read_excel("/Users/junhyeongkim/Desktop/lab_project/prostate_data.xlsx")

# Split the data into two groups based on the diagnosis (e.g. prostate cancer or not)
group_a = df[df['Sample'].str.contains("HC")]['OR2W1']
group_b = df[df['Sample'].str.contains("LPC")]['OR2W1']

# Perform the two-sample t-test
t, p = stats.ttest_ind(group_a, group_b)

# Print the t-statistic and p-value
print("t-statistic:", t)
print("p-value:", p)

# Interpret the results
alpha = 0.05
if p > alpha:
    print("Fail to reject the null hypothesis, the means of the two groups are not significantly different.")
else:
    print("Reject the null hypothesis, the means of the two groups are significantly different.")

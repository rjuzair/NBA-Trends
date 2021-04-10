import numpy as np
import pandas as pd
from scipy.stats import pearsonr, chi2_contingency
import matplotlib.pyplot as plt
import seaborn as sns

import codecademylib3
np.set_printoptions(suppress=True, precision = 2)

nba = pd.read_csv('./nba_games.csv')

# Subset Data to 2010 Season, 2014 Season
nba_2010 = nba[nba.year_id == 2010]
nba_2014 = nba[nba.year_id == 2014]

print(nba_2010.head())
print(nba_2014.head())

knicks_pts = nba_2010.pts[nba_2010.fran_id == 'Knicks']
nets_pts = nba_2010.pts[nba_2010.fran_id == 'Nets']

knicks_mean_score = np.mean(knicks_pts)
nets_mean_score = np.mean(nets_pts)
diff_mean = knicks_mean_score - nets_mean_score
print(diff_mean)

plt.clf()
plt.hist(knicks_pts, alpha = 0.8, normed = True, label = 'Knicks')
plt.hist(nets_pts, alpha = 0.8, normed = True, label = 'Nets')
plt.legend()
plt.show()

knicks_pts = nba_2014.pts[nba_2014.fran_id == 'Knicks']
nets_pts = nba_2014.pts[nba_2014.fran_id == 'Nets']

knicks_mean_score = np.mean(knicks_pts)
nets_mean_score = np.mean(nets_pts)
diff_mean = knicks_mean_score - nets_mean_score
print(diff_mean)

plt.clf()
plt.hist(knicks_pts, alpha = 0.8, normed = True, label = 'Knicks')
plt.hist(nets_pts, alpha = 0.8, normed = True, label = 'Nets')
plt.legend()
plt.show()

plt.clf()
sns.boxplot(data = nba_2010, x = 'fran_id', y = 'pts')
plt.show()

location_results_freq = pd.crosstab(
  nba_2010.game_result,
  nba_2010.game_location
)
print(location_results_freq)

location_result_proportions = location_results_freq / len(nba_2010) * 100
print(location_result_proportions)

chi2, pval, dof, expected = chi2_contingency(location_results_freq)
print(expected)
print(chi2)

result = np.cov(nba_2010.forecast, nba_2010.point_diff)
print(result)

result = pearsonr(nba_2010.forecast, nba_2010.point_diff)
print(result)

plt.clf()
plt.scatter('forecast', 'point_diff', data = nba_2010)
plt.title('Table')
plt.show()

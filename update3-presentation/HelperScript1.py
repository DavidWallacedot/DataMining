 
import pandas as pd
import numpy as np
import cliffsDelta

def compareLists(defective_vals_for_feature, non_defective_vals_for_feature):
          '''
          summary time
          '''
          print ('='*25)
          print ("Defective values [MEDIAN]:{}, [MEAN]:{}, [COUNT]:{}".format(np.median(list(defective_vals_for_feature)), np.mean(list(defective_vals_for_feature)), len(defective_vals_for_feature)))
          print ("Non Defective values [MEDIAN]:{}, [MEAN]:{}, [COUNT]:{}".format(np.median(list(non_defective_vals_for_feature)), np.mean(list(non_defective_vals_for_feature)), len(non_defective_vals_for_feature)))
          try:
             TS, p = stats.mannwhitneyu(list(defective_vals_for_feature), list(non_defective_vals_for_feature), alternative='greater')
          except ValueError:
             TS, p = 0.0, 1.0
          cliffs_delta = cliffsDelta.cliffsDelta(list(defective_vals_for_feature), list(non_defective_vals_for_feature))
          print ('*'*25)
          print ('Feature:{}, pee value:{}, cliffs:{}'.format(feature_, p, cliffs_delta))
          print ('*'*25)
          print ('='*50)
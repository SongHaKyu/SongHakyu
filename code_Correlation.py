## data_Correlation
plt.figure(figsize=(10,10))
sns.heatmap(train_input.corr(),cmap = 'coolwarm',linewidth = 1,annot= True, annot_kws={"size": 9})
plt.title('Variable Correlation')

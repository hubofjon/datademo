#Author: JonQLi
def feature_plot(df):
    
    df.sort_index(1)
    
    import matplotlib.pyplot as plt
    #assign color based on win_22 True or False
    rows=df.shape[0]

    cols=df.shape[1]
    #pcolor="blue"
    for i in range(rows):
#       if df.iloc[i,cols-1]>=0.9:
        if df.iloc[i,cols-1]=='SS':
            pcolor="blue"
        else: 
            pcolor="yellow"
#        #plot rows of data as if they were series data
#        datarow=df.iloc[i,0:cols-1]
#        datarow.plot(color=pcolor, alpha=0.7)
        
        datarow=df.iloc[i,:cols-1]
        #datarow=datarow.astype(float)
        datarow.plot(color=pcolor, alpha=0.3)
       
    locs, labels = plt.xticks()   
    plt.xlabel("feature index")
    #plt.ylabel("win_lose")
    labels=df.columns
    
    locs=np.arange(labels.shape[0])
    plt.xticks( locs, labels, rotation=90 )
    #ax.set_xticks(labels, minor=True)
    #print (locs)
    plt.show()
	
def ml_linear(df):
    import sklearn.metrics as sm

    lr = linear_model.LinearRegression()
       #y=y.applymap(lambda x:1 if x else 0)
  #split dataset
    
    #df.rename(columns={'rtn_22_fwd_pct':'zrtn_22_fwd_pct'}, inplace=True)  
    df.sort_index(axis=1)
    x=df.iloc[:,:-1]
    y=df.iloc[:,df.shape[1]-1]
    x=x.values
    x=pre_process(x)
    y=y.values
    #print (x.shape, y.shape)
    x_train, x_test, y_train, y_test= train_test_split(x,y, train_size = 0.8)
    #print (x_train.shape, y_train.shape)
#standardize features
    scaler= preprocessing.StandardScaler().fit(x_train)    
    x_train=scaler.transform(x_train)
    x_test=scaler.transform(x_test)
    
    lr.fit(x_train, y_train)

    y_test_pred=lr.predict(x_test)
    error=y_test-y_test_pred
    
    print ("Mean absolute error =", round(sm.mean_absolute_error(y_test, y_test_pred), 2) )
    return y_test_pred, y_test

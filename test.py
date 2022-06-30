from cmath import nan
from mmap import PAGESIZE
import openfoodfacts as client
import pandas as pd

#testing basic search for product in openfoodfacts
#print(response)
#dict = atr response['products'][0].keys()



##*******************************************************

#CONVERTING THE DATAFRAME INTO A CSV
#response = client.products.search({},page_size = 20, locale='dz')
#df = pd.DataFrame.from_dict(response['products']) 

#df.to_csv('test.csv')

##*******************************************************


##*******************************************************
##HERE I WAS TRYING TO MAKE A LIST OF ALL THE ATTRIBUTES:

#response = client.products.search({},page_size = 20, locale='dz')
#df = pd.DataFrame.from_dict(response['products']) 
#for item in df.columns:
#    print(item)
##*******************************************************

##*******************************************************
##DISPLAYING A DATA FRAME WITH CERTAIN ATTRIBUTES
#response = client.products.search({},page_size = 20, locale='dz')
#df = pd.DataFrame.from_dict(response['products']) 
#print(df[['_id', 'brands', 'generic_name', 'product_name_fi', 'generic_name_fr']])
##*******************************************************



##LOOPING THROUGH ALL THE PRODUCTS AND MAKING A COMPARAISON BETWEEN TWO ATTRIBUTES
""" cond = True
i=1
while(cond): 
    response = client.products.search({},page=i, page_size =20 , locale='dz')
    df = pd.DataFrame.from_dict(response['products'])
    print(df[['_id', 'brands', 'generic_name', 'generic_name_fr']])
    i=i+1
    if(i>162):
        print('XDDDDDDDDDDDDDddd')
        cond = False """
##TESTING TO SEE THE ATTRIBUTES THAT ARE ALWAYS THERE AND WRITING THAT TO A FILE
rankdict={}
for i in range(150):
    response = client.products.search({},page_size = 20, page=i+1, locale='dz')
    df = pd.DataFrame.from_dict(response['products'])
    """ liist = []
    for item in df.columns:
        liist.append(item)
    for item in liist:
        if str(df.loc[2,item])!='nan' and str(df.loc[2,item])!='' and str(df.loc[2,item])!='[]':
            print(item) """ 


    for column in df:
        i=0
        for value in df[column]:
            if str(value)!='nan' and str(value)!='' and str(value)!='[]':
                i=i+1
        try :
            rankdict[column]=rankdict[column]+i
        except :
            rankdict[column]=i
for key,value in rankdict.items():
    rankdict[key]= rankdict[key]/150
f = open("TEST ATTRIBUTES.txt", "w")
for key, value in sorted(rankdict.items(),
                        key=lambda item: item[1]):
    f.write('{} :: {}\n'.format(key, value))
""" 
response = client.products.search({},page=1, page_size =40 , locale='dz')
df = pd.DataFrame.from_dict(response['products'])

print(df[['_id', 'brands', 'product_name', 'code']]) """
## NOTE code _id and id are the same 

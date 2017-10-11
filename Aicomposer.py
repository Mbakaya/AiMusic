import urllib
import zipfile
import nottingham_util
import rnn

#finding our dataset zip using urllib from the given url
url = "www-etud.iro.umontreal.ca/~boulanni/Nottingham.zip"
urllib.urlretrieve(url,"dataset.zip")

#extract the zipfile to gt the data
zip = zipfile.ZipFile(r'dataset.zip')
zip.extractall('data')

nottingham_util.create_model()
#call train model method  of neural net class
rnn.train_model()

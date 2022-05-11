import os
acc = os. popen ("sudo cat /mnt/accuracy.txt")
ac = float(acc.read).rstrip)
print (acc)

if acc < 0.90:
file = os. popen("sudo cat /code/model jonah.py | grep HP_EPOCHS -m 1 | grep -Eo [0-9]")
epoch = int(file.read).replace("\n", ""))
print ("current number of epochs are”, epoch)
epoch = epoch + 10
print ("updated number of epochs are”, epoch)
print (type(epoch))
update = "HP_EPOCHS={}".format(int(epoch))
print (update)
os.system("sudo sed -i 's/.*HP _EPOCHS=.*/{}/' /code/model_jonah.py".format(update))
file = os.popen("sudo cat /code/model_jonah.py | grep HP_BS -m 1 | grep -Eo [0-9]")
bs = int(file.read().replace("\n",""))
print ("current batch size is ", bs)
bs = bs + 5
print ("updated batch size is ", bs)
print (type(bs))
update = "HP BS={}".format(int(bs))
print (update)
os.system("sudo sed -i 'S/.*HP_BS=.*/{}/" /code/model jonah.py".format(update))

os.system("curl -u admin: admin http://65.0.89.249:8080/job/major_project_Job_1/build?token=jobl")

else:
print ("good accuracy")

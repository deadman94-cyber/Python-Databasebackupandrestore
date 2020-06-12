import psycopg2
import os
import sys
#import gzip
#import subprocess 
print("Here we gonna take Database Backup")


ip = input("Enter the god damn IP = ")
name=input("Enter the god damn of the database User = ")
datab=input("Enter the god damn of the database Name = " )

def backup():
    conn = None
    try:
        conn = psycopg2.connect(host=ip,database=datab,user=name)
        dname = input("Enter the name you want to keep database as = ")
        dpath=input("Enter the path where you want to keep the backup = ")
        os.system('pg_dump -U {0} -d {1} -f {2}/{3}.sql'.format(name,datab,dpath,dname))
        #os.system('cd {0}'.format(dpath))
        print(os.system('pwd'))
        #os.system('zip -r {0}/{1}.sql.zip {0}/{1}.sql'.format(dpath,dname))
        os.system('gzip {0}/{1}.sql'.format(dpath,dname))
        print("Now Deleting sql file") 
        os.system('rm -rf {0}/{1}.sql'.format(dpath,dname))
        #output=stream.read()
        #output
    except(Exception,psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            print("Database Backup Done and sql removed")


if __name__ =='__main__':
    backup()



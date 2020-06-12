import psycopg2
import os

print("Here we gonna restore the database Backup")
ip = input("Enter the god damn IP = ")
name=input("Enter the god damn of the database User = ")
datab=input("Enter the god damn of the database Name you want to create = " )
def restore():
    conn = None
    try:
        con = psycopg2.connect(host=ip,user=name)
        #os.system('psql -U {0}'.format(name))
        con.autocommit = True

        cur = con.cursor()
        cur.execute('create database {0};'.format(datab))
        cur.close()
        print("{0} Database has been created".format(datab))
        dpath=input("Enter the path where backup = ")
        n=input("enter name of file only name =")
        os.system('gunzip {0}/{1}.sql.gz '.format(dpath,n))
        os.system('psql -U {0} -d {1} -f {2}.sql '.format(name,datab,n))
        os.system('rm -rf {0}.sql'.format(n))        
        
    except(Exception,psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            print("ok")


if __name__ =='__main__':
    restore()

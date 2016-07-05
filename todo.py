import os,django,sys,click,openpyxl
sys.path.append("F:\Summer\AssignmentProject")
os.environ["DJANGO_SETTINGS_MODULE"] = "AssignmentProject.settings"
django.setup()
import MySQLdb
from Todos.models import *
db = MySQLdb.connect(host="localhost", port=90, user="root", passwd="admin", db="mysql")
cursor = db.cursor()
@click.group()
def cli():
    pass

@cli.command()
#@click.argument('username',nargs=1,click.Path.type)
def createdb():
    try:
        cursor.execute("create database todosproject")
        print "database created"
    except:
        print "database alreay exits"
    os.system("python manage.py makemigrations")
    os.system("python manage.py migrate")

@cli.command()
def dropdb():
    cursor.execute("DROP DATABASE IF EXISTS todosproject")
    print "database droped"

@cli.command(help="store data in database")
def populate():
    for i in range(1,11):
        tlist=TodoList(name='todolist'+str(i),date=datetime.date(2016,06,1))
        tlist.save()
    lists=TodoList.objects.all()
    for i in range(1,11):
        for j in range(1,6):
            titem=TodoItem(item_id_id=lists.get(id=i).id,description="description"+str(j),duedate=datetime.date(2016,06,19),status=False)
            titem.save()

@cli.command(help="clear data in database")
def clear():
    TodoItem.objects.all().delete()
    TodoList.objects.all().delete()



if __name__ =='__main__':
    cli()
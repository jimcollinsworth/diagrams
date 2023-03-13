from common import *

def all_icons():
    ''' display legend of all diagram icons imported 
    Hardcoded currently, should be a meta function, get all imported functions from 'diagrams.*'
    '''
    with Cluster("Icons"):
        #Diagram("Diagram")
        #Cluster("Cluster")
        pass

with Diagram("all icons", show=False):
    #all_icons()
    with Cluster("Cluster 1") as cluster1:
        Angular("Angular") - Django("Django") - Python("Python") - JavaScript("JavaScript") - NodeJS("NodeJS") - Bash("Bash")
        Twitter("Twitter") - PowerBI("PowerBI") - Tableau("Tableau") - Jenkins("Jenkins") - Git("Git") - Docker("Docker")
        Blank("Blank") - Mobile("Mobile") - Edge(color="firebrick", style="dashed") -Tablet("Tablet") - Client("Client") - User("User") - Users("Users") 
        VPN("VPN") - Firewall("Firewall") - Subnet("Subnet") - Switch("Switch") - Rack("Rack") - Datacenter("Datacenter") - Storage("Storage") - Server("Server")  
        Windows("Windows") - Ubuntu("Ubuntu") - Kibana("Kibana") - ElasticSearch("ElasticSearch") - Spark("Spark") - MongoDB("MongoDB") - PostgreSQL("PostgreSQL") - Dynatrace("Dynatrace") - Internet("Internet") - Apache("Apache")
        InputOutput("InputOutput") - InternalStorage("InternalStorage") - PredefinedProcess("PredefinedProcess") - Display("Display") - Document("Document", ) - MultipleDocuments("MultipleDocuments") - Database("Database") - Action("Action") 
    
    with Cluster("Cluster 2") as cluster2:
        with SystemBoundary("System Boundary"):
            webapp = Container(
                name="Web Application",
                technology="Java and Spring MVC",
                description="Delivers the static content and the Internet banking single page application.",
            )
        Person("Person Title", description="Person Description", external=True) >> Relationship("Relationship") >> webapp << C4Database("C4Database") - System("System") - Container("Container")


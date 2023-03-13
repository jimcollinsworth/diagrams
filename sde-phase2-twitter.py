from diagrams import Diagram, Cluster, Edge
from diagrams.elastic.elasticsearch import Kibana, ElasticSearch
from diagrams.programming.framework import Angular, Django
from diagrams.programming.language import Python, JavaScript, NodeJS, Bash
from diagrams.saas.social import Twitter
from diagrams.onprem.analytics import Spark, PowerBI, Tableau
from diagrams.onprem.ci import Jenkins # rundeck?
from diagrams.onprem.client import Client, User, Users
from diagrams.onprem.compute import Server
from diagrams.onprem.database import MongoDB, PostgreSQL
from diagrams.onprem.monitoring import Dynatrace
from diagrams.onprem.network import Apache, Internet
from diagrams.onprem.vcs import Git # bitbucket
from diagrams.onprem.container import Docker
from diagrams.generic.blank import Blank
from diagrams.generic.compute import Rack
from diagrams.generic.device import Mobile, Tablet
from diagrams.generic.network import VPN, Firewall, Subnet, Switch
from diagrams.generic.os import Windows, Ubuntu
from diagrams.generic.place import Datacenter
from diagrams.generic.storage import Storage
from diagrams.programming.flowchart import Action, InputOutput, InternalStorage, Database, Display, Document, MultipleDocuments
from diagrams.programming.flowchart import PredefinedProcess
from diagrams.c4 import Person, Container, Database as C4Database, System, SystemBoundary, Relationship

with Diagram("HMC Dashboard and SDE", show=False):
    with Cluster("Twitter API") as twitter_api:
        one_per = Twitter("1% feed")
        hpt = Twitter("GNIP-HPT")
        archive_search = Twitter("Archive Search")
        filtered_search = Twitter("Filtered Search")

    with Cluster("Other APIs, Feeds") as other_api:
        reddit = Container("Reddit API")
        activity_pub = Container("Activity PUB")
        p_drive = Container("P drive file")  
 
    with Cluster("Data Ingestion") as data_injestion:
        stream = Container("Stream Feed")
        filtered_stream = Container("Filtered Stream")
        archive_search = Container("Archive Search")
        
    with Cluster("Data Science 'Cluster'") as ds_cluster: 
        rules_db = Database(
            name="Rules Database",
            technology="Mongodb",
            description="Stores GNIP/HPT rules, tweets and rule/tag counts",
        )

        es_db = Database(
            name="Social Database",
            technology="Elastic Search Cluster",
            description="Stores indexes, metadata, Tweets, query results; enables fast search, aggregation, data enhancement",
        )

        app_db = Database(
            name="DE Application Database",
            technology="Django/Postgres",
            description="Stores explorer user/project metadata",
        )



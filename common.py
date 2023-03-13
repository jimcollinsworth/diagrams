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
from common import *

''' Current HMC Dashboard and SDE architectures

'''

hmc_node_attributes = {"fillcolor": "bisque"}
sde_node_attributes = {"fillcolor": "azure"}

with Diagram("HMC Dashboard and SDE", show=False):
    with Cluster("Legend") as legend:
        hmc = Container(name="HMC Dashboard")
        sde = Container(name="Social Data Explorer")

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
        rules_db = C4Database(
            name="Rules Database",
            technology="Mongodb",
            description="Stores GNIP/HPT rules, tweets and rule/tag counts",
        )

        es_db = C4Database(
            name="Social Database",
            technology="Elastic Search Cluster",
            description="Stores indexes, metadata, Tweets, query results; enables fast search, aggregation, data enhancement",
        )

        app_db = C4Database(
            name="DE Application Database",
            technology="Django/Postgres",
            description="Stores explorer user/project metadata",
        )



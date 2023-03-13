from common import *

''' SDE Phase 2 with open social network support, Norc Twitter Archive access, Twitter access*

    Supports any current and future social network
    Flexible and efficient ingestion modules in Spark
    Multi-social network data indexing, augmentation, search, aggregation in Elastic Search
    Search/aggregation data vizualization with Kibana
    More capabilities with Elastic Stack and add ins.
    Easy data exports for external reporting 
    APIs for metadata, ingestion, query, social data for Python and R 
    With the expected API costs, maybe no more Twitter data for SDE, only HPT & 1% 2016-2023.
'''

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



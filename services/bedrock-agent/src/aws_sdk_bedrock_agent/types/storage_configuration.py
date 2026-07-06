"""Generated from Smithy shape ``com.amazonaws.bedrockagent#StorageConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.knowledge_base_storage_type
    import aws_sdk_bedrock_agent.types.mongo_db_atlas_configuration
    import aws_sdk_bedrock_agent.types.neptune_analytics_configuration
    import aws_sdk_bedrock_agent.types.open_search_managed_cluster_configuration
    import aws_sdk_bedrock_agent.types.open_search_serverless_configuration
    import aws_sdk_bedrock_agent.types.pinecone_configuration
    import aws_sdk_bedrock_agent.types.rds_configuration
    import aws_sdk_bedrock_agent.types.redis_enterprise_cloud_configuration
    import aws_sdk_bedrock_agent.types.s3_vectors_configuration


class StorageConfiguration(TypedDict, closed=True):
    type: "aws_sdk_bedrock_agent.types.knowledge_base_storage_type.KnowledgeBaseStorageType"
    """<p>The vector store service in which the knowledge base is stored.</p>"""
    opensearch_serverless_configuration: NotRequired[
        "aws_sdk_bedrock_agent.types.open_search_serverless_configuration.OpenSearchServerlessConfiguration"
    ]
    """<p>Contains the storage configuration of the knowledge base in Amazon OpenSearch Service.</p>"""
    opensearch_managed_cluster_configuration: NotRequired[
        "aws_sdk_bedrock_agent.types.open_search_managed_cluster_configuration.OpenSearchManagedClusterConfiguration"
    ]
    r"""<p>Contains details about the storage configuration of the knowledge base in OpenSearch Managed Cluster. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup-osm.html\">Create a vector index in Amazon OpenSearch Service</a>.</p>"""
    pinecone_configuration: NotRequired[
        "aws_sdk_bedrock_agent.types.pinecone_configuration.PineconeConfiguration"
    ]
    """<p>Contains the storage configuration of the knowledge base in Pinecone.</p>"""
    redis_enterprise_cloud_configuration: NotRequired[
        "aws_sdk_bedrock_agent.types.redis_enterprise_cloud_configuration.RedisEnterpriseCloudConfiguration"
    ]
    """<p>Contains the storage configuration of the knowledge base in Redis Enterprise Cloud.</p>"""
    rds_configuration: NotRequired[
        "aws_sdk_bedrock_agent.types.rds_configuration.RdsConfiguration"
    ]
    r"""<p>Contains details about the storage configuration of the knowledge base in Amazon RDS. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup-rds.html\">Create a vector index in Amazon RDS</a>.</p>"""
    mongo_db_atlas_configuration: NotRequired[
        "aws_sdk_bedrock_agent.types.mongo_db_atlas_configuration.MongoDbAtlasConfiguration"
    ]
    """<p>Contains the storage configuration of the knowledge base in MongoDB Atlas.</p>"""
    neptune_analytics_configuration: NotRequired[
        "aws_sdk_bedrock_agent.types.neptune_analytics_configuration.NeptuneAnalyticsConfiguration"
    ]
    r"""<p>Contains details about the Neptune Analytics configuration of the knowledge base in Amazon Neptune. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup-neptune.html\">Create a vector index in Amazon Neptune Analytics.</a>.</p>"""
    s3_vectors_configuration: NotRequired[
        "aws_sdk_bedrock_agent.types.s3_vectors_configuration.S3VectorsConfiguration"
    ]
    """<p>The configuration settings for storing knowledge base data using S3 vectors. This includes vector index information and S3 bucket details for vector storage.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StorageConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.knowledge_base_storage_type

    out["type"] = (
        aws_sdk_bedrock_agent.types.knowledge_base_storage_type.serialize_json(
            value["type"]
        )
    )
    if "opensearch_serverless_configuration" in value:
        import aws_sdk_bedrock_agent.types.open_search_serverless_configuration

        out["opensearchServerlessConfiguration"] = (
            aws_sdk_bedrock_agent.types.open_search_serverless_configuration.serialize_json(
                value["opensearch_serverless_configuration"]
            )
        )
    if "opensearch_managed_cluster_configuration" in value:
        import aws_sdk_bedrock_agent.types.open_search_managed_cluster_configuration

        out["opensearchManagedClusterConfiguration"] = (
            aws_sdk_bedrock_agent.types.open_search_managed_cluster_configuration.serialize_json(
                value["opensearch_managed_cluster_configuration"]
            )
        )
    if "pinecone_configuration" in value:
        import aws_sdk_bedrock_agent.types.pinecone_configuration

        out["pineconeConfiguration"] = (
            aws_sdk_bedrock_agent.types.pinecone_configuration.serialize_json(
                value["pinecone_configuration"]
            )
        )
    if "redis_enterprise_cloud_configuration" in value:
        import aws_sdk_bedrock_agent.types.redis_enterprise_cloud_configuration

        out["redisEnterpriseCloudConfiguration"] = (
            aws_sdk_bedrock_agent.types.redis_enterprise_cloud_configuration.serialize_json(
                value["redis_enterprise_cloud_configuration"]
            )
        )
    if "rds_configuration" in value:
        import aws_sdk_bedrock_agent.types.rds_configuration

        out["rdsConfiguration"] = (
            aws_sdk_bedrock_agent.types.rds_configuration.serialize_json(
                value["rds_configuration"]
            )
        )
    if "mongo_db_atlas_configuration" in value:
        import aws_sdk_bedrock_agent.types.mongo_db_atlas_configuration

        out["mongoDbAtlasConfiguration"] = (
            aws_sdk_bedrock_agent.types.mongo_db_atlas_configuration.serialize_json(
                value["mongo_db_atlas_configuration"]
            )
        )
    if "neptune_analytics_configuration" in value:
        import aws_sdk_bedrock_agent.types.neptune_analytics_configuration

        out["neptuneAnalyticsConfiguration"] = (
            aws_sdk_bedrock_agent.types.neptune_analytics_configuration.serialize_json(
                value["neptune_analytics_configuration"]
            )
        )
    if "s3_vectors_configuration" in value:
        import aws_sdk_bedrock_agent.types.s3_vectors_configuration

        out["s3VectorsConfiguration"] = (
            aws_sdk_bedrock_agent.types.s3_vectors_configuration.serialize_json(
                value["s3_vectors_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> StorageConfiguration:
    out: StorageConfiguration = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_bedrock_agent.types.knowledge_base_storage_type

        out["type"] = (
            aws_sdk_bedrock_agent.types.knowledge_base_storage_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError("StorageConfiguration.type required")
    if "opensearchServerlessConfiguration" in data:
        import aws_sdk_bedrock_agent.types.open_search_serverless_configuration

        out["opensearch_serverless_configuration"] = (
            aws_sdk_bedrock_agent.types.open_search_serverless_configuration.deserialize_json(
                data["opensearchServerlessConfiguration"]
            )
        )
    if "opensearchManagedClusterConfiguration" in data:
        import aws_sdk_bedrock_agent.types.open_search_managed_cluster_configuration

        out["opensearch_managed_cluster_configuration"] = (
            aws_sdk_bedrock_agent.types.open_search_managed_cluster_configuration.deserialize_json(
                data["opensearchManagedClusterConfiguration"]
            )
        )
    if "pineconeConfiguration" in data:
        import aws_sdk_bedrock_agent.types.pinecone_configuration

        out["pinecone_configuration"] = (
            aws_sdk_bedrock_agent.types.pinecone_configuration.deserialize_json(
                data["pineconeConfiguration"]
            )
        )
    if "redisEnterpriseCloudConfiguration" in data:
        import aws_sdk_bedrock_agent.types.redis_enterprise_cloud_configuration

        out["redis_enterprise_cloud_configuration"] = (
            aws_sdk_bedrock_agent.types.redis_enterprise_cloud_configuration.deserialize_json(
                data["redisEnterpriseCloudConfiguration"]
            )
        )
    if "rdsConfiguration" in data:
        import aws_sdk_bedrock_agent.types.rds_configuration

        out["rds_configuration"] = (
            aws_sdk_bedrock_agent.types.rds_configuration.deserialize_json(
                data["rdsConfiguration"]
            )
        )
    if "mongoDbAtlasConfiguration" in data:
        import aws_sdk_bedrock_agent.types.mongo_db_atlas_configuration

        out["mongo_db_atlas_configuration"] = (
            aws_sdk_bedrock_agent.types.mongo_db_atlas_configuration.deserialize_json(
                data["mongoDbAtlasConfiguration"]
            )
        )
    if "neptuneAnalyticsConfiguration" in data:
        import aws_sdk_bedrock_agent.types.neptune_analytics_configuration

        out["neptune_analytics_configuration"] = (
            aws_sdk_bedrock_agent.types.neptune_analytics_configuration.deserialize_json(
                data["neptuneAnalyticsConfiguration"]
            )
        )
    if "s3VectorsConfiguration" in data:
        import aws_sdk_bedrock_agent.types.s3_vectors_configuration

        out["s3_vectors_configuration"] = (
            aws_sdk_bedrock_agent.types.s3_vectors_configuration.deserialize_json(
                data["s3VectorsConfiguration"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.bedrockagent#MongoDbAtlasConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.mongo_db_atlas_collection_name
    import aws_sdk_bedrock_agent.types.mongo_db_atlas_database_name
    import aws_sdk_bedrock_agent.types.mongo_db_atlas_endpoint
    import aws_sdk_bedrock_agent.types.mongo_db_atlas_endpoint_service_name
    import aws_sdk_bedrock_agent.types.mongo_db_atlas_field_mapping
    import aws_sdk_bedrock_agent.types.mongo_db_atlas_index_name
    import aws_sdk_bedrock_agent.types.secret_arn


class MongoDbAtlasConfiguration(TypedDict):
    endpoint: "aws_sdk_bedrock_agent.types.mongo_db_atlas_endpoint.MongoDbAtlasEndpoint"
    """<p>The endpoint URL of your MongoDB Atlas cluster for your knowledge base.</p>"""
    database_name: "aws_sdk_bedrock_agent.types.mongo_db_atlas_database_name.MongoDbAtlasDatabaseName"
    """<p>The database name in your MongoDB Atlas cluster for your knowledge base.</p>"""
    collection_name: "aws_sdk_bedrock_agent.types.mongo_db_atlas_collection_name.MongoDbAtlasCollectionName"
    """<p>The collection name of the knowledge base in MongoDB Atlas.</p>"""
    vector_index_name: (
        "aws_sdk_bedrock_agent.types.mongo_db_atlas_index_name.MongoDbAtlasIndexName"
    )
    """<p>The name of the MongoDB Atlas vector search index.</p>"""
    credentials_secret_arn: "aws_sdk_bedrock_agent.types.secret_arn.SecretArn"
    """<p>The Amazon Resource Name (ARN) of the secret that you created in Secrets Manager that contains user credentials for your MongoDB Atlas cluster.</p>"""
    field_mapping: "aws_sdk_bedrock_agent.types.mongo_db_atlas_field_mapping.MongoDbAtlasFieldMapping"
    """<p>Contains the names of the fields to which to map information about the vector store.</p>"""
    endpoint_service_name: NotRequired[
        "aws_sdk_bedrock_agent.types.mongo_db_atlas_endpoint_service_name.MongoDbAtlasEndpointServiceName"
    ]
    """<p>The name of the VPC endpoint service in your account that is connected to your MongoDB Atlas cluster.</p>"""
    text_index_name: NotRequired[
        "aws_sdk_bedrock_agent.types.mongo_db_atlas_index_name.MongoDbAtlasIndexName"
    ]
    """<p>The name of the text search index in the MongoDB collection. This is required for using the hybrid search feature.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MongoDbAtlasConfiguration) -> dict:
    out: dict = {}
    out["endpoint"] = value["endpoint"]
    out["databaseName"] = value["database_name"]
    out["collectionName"] = value["collection_name"]
    out["vectorIndexName"] = value["vector_index_name"]
    out["credentialsSecretArn"] = value["credentials_secret_arn"]
    import aws_sdk_bedrock_agent.types.mongo_db_atlas_field_mapping

    out["fieldMapping"] = (
        aws_sdk_bedrock_agent.types.mongo_db_atlas_field_mapping.serialize_json(
            value["field_mapping"]
        )
    )
    if "endpoint_service_name" in value:
        out["endpointServiceName"] = value["endpoint_service_name"]
    if "text_index_name" in value:
        out["textIndexName"] = value["text_index_name"]
    return out


def deserialize_json(data: dict) -> MongoDbAtlasConfiguration:
    out: MongoDbAtlasConfiguration = {}  # type: ignore[typeddict-item]
    if "endpoint" in data:
        out["endpoint"] = data["endpoint"]
    else:
        raise DeserializationError("MongoDbAtlasConfiguration.endpoint required")
    if "databaseName" in data:
        out["database_name"] = data["databaseName"]
    else:
        raise DeserializationError("MongoDbAtlasConfiguration.database_name required")
    if "collectionName" in data:
        out["collection_name"] = data["collectionName"]
    else:
        raise DeserializationError("MongoDbAtlasConfiguration.collection_name required")
    if "vectorIndexName" in data:
        out["vector_index_name"] = data["vectorIndexName"]
    else:
        raise DeserializationError(
            "MongoDbAtlasConfiguration.vector_index_name required"
        )
    if "credentialsSecretArn" in data:
        out["credentials_secret_arn"] = data["credentialsSecretArn"]
    else:
        raise DeserializationError(
            "MongoDbAtlasConfiguration.credentials_secret_arn required"
        )
    if "fieldMapping" in data:
        import aws_sdk_bedrock_agent.types.mongo_db_atlas_field_mapping

        out["field_mapping"] = (
            aws_sdk_bedrock_agent.types.mongo_db_atlas_field_mapping.deserialize_json(
                data["fieldMapping"]
            )
        )
    else:
        raise DeserializationError("MongoDbAtlasConfiguration.field_mapping required")
    if "endpointServiceName" in data:
        out["endpoint_service_name"] = data["endpointServiceName"]
    if "textIndexName" in data:
        out["text_index_name"] = data["textIndexName"]
    return out

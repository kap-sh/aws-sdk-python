"""Generated from Smithy shape ``com.amazonaws.bedrockagent#RedisEnterpriseCloudConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.redis_enterprise_cloud_endpoint
    import aws_sdk_bedrock_agent.types.redis_enterprise_cloud_field_mapping
    import aws_sdk_bedrock_agent.types.redis_enterprise_cloud_index_name
    import aws_sdk_bedrock_agent.types.secret_arn


class RedisEnterpriseCloudConfiguration(TypedDict, closed=True):
    endpoint: "aws_sdk_bedrock_agent.types.redis_enterprise_cloud_endpoint.RedisEnterpriseCloudEndpoint"
    """<p>The endpoint URL of the Redis Enterprise Cloud database.</p>"""
    vector_index_name: "aws_sdk_bedrock_agent.types.redis_enterprise_cloud_index_name.RedisEnterpriseCloudIndexName"
    """<p>The name of the vector index.</p>"""
    credentials_secret_arn: "aws_sdk_bedrock_agent.types.secret_arn.SecretArn"
    """<p>The Amazon Resource Name (ARN) of the secret that you created in Secrets Manager that is linked to your Redis Enterprise Cloud database.</p>"""
    field_mapping: "aws_sdk_bedrock_agent.types.redis_enterprise_cloud_field_mapping.RedisEnterpriseCloudFieldMapping"
    """<p>Contains the names of the fields to which to map information about the vector store.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RedisEnterpriseCloudConfiguration) -> dict:
    out: dict = {}
    out["endpoint"] = value["endpoint"]
    out["vectorIndexName"] = value["vector_index_name"]
    out["credentialsSecretArn"] = value["credentials_secret_arn"]
    import aws_sdk_bedrock_agent.types.redis_enterprise_cloud_field_mapping

    out["fieldMapping"] = (
        aws_sdk_bedrock_agent.types.redis_enterprise_cloud_field_mapping.serialize_json(
            value["field_mapping"]
        )
    )
    return out


def deserialize_json(data: dict) -> RedisEnterpriseCloudConfiguration:
    out: RedisEnterpriseCloudConfiguration = {}  # type: ignore[typeddict-item]
    if "endpoint" in data:
        out["endpoint"] = data["endpoint"]
    else:
        raise DeserializationError(
            "RedisEnterpriseCloudConfiguration.endpoint required"
        )
    if "vectorIndexName" in data:
        out["vector_index_name"] = data["vectorIndexName"]
    else:
        raise DeserializationError(
            "RedisEnterpriseCloudConfiguration.vector_index_name required"
        )
    if "credentialsSecretArn" in data:
        out["credentials_secret_arn"] = data["credentialsSecretArn"]
    else:
        raise DeserializationError(
            "RedisEnterpriseCloudConfiguration.credentials_secret_arn required"
        )
    if "fieldMapping" in data:
        import aws_sdk_bedrock_agent.types.redis_enterprise_cloud_field_mapping

        out["field_mapping"] = (
            aws_sdk_bedrock_agent.types.redis_enterprise_cloud_field_mapping.deserialize_json(
                data["fieldMapping"]
            )
        )
    else:
        raise DeserializationError(
            "RedisEnterpriseCloudConfiguration.field_mapping required"
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.bedrockagent#RedshiftQueryEngineStorageConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.redshift_query_engine_aws_data_catalog_storage_configuration
    import aws_sdk_bedrock_agent.types.redshift_query_engine_redshift_storage_configuration
    import aws_sdk_bedrock_agent.types.redshift_query_engine_storage_type


class RedshiftQueryEngineStorageConfiguration(TypedDict):
    type: "aws_sdk_bedrock_agent.types.redshift_query_engine_storage_type.RedshiftQueryEngineStorageType"
    """<p>The data storage service to use.</p>"""
    aws_data_catalog_configuration: NotRequired[
        "aws_sdk_bedrock_agent.types.redshift_query_engine_aws_data_catalog_storage_configuration.RedshiftQueryEngineAwsDataCatalogStorageConfiguration"
    ]
    """<p>Specifies configurations for storage in Glue Data Catalog.</p>"""
    redshift_configuration: NotRequired[
        "aws_sdk_bedrock_agent.types.redshift_query_engine_redshift_storage_configuration.RedshiftQueryEngineRedshiftStorageConfiguration"
    ]
    """<p>Specifies configurations for storage in Amazon Redshift.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RedshiftQueryEngineStorageConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.redshift_query_engine_storage_type

    out["type"] = (
        aws_sdk_bedrock_agent.types.redshift_query_engine_storage_type.serialize_json(
            value["type"]
        )
    )
    if "aws_data_catalog_configuration" in value:
        import aws_sdk_bedrock_agent.types.redshift_query_engine_aws_data_catalog_storage_configuration

        out["awsDataCatalogConfiguration"] = (
            aws_sdk_bedrock_agent.types.redshift_query_engine_aws_data_catalog_storage_configuration.serialize_json(
                value["aws_data_catalog_configuration"]
            )
        )
    if "redshift_configuration" in value:
        import aws_sdk_bedrock_agent.types.redshift_query_engine_redshift_storage_configuration

        out["redshiftConfiguration"] = (
            aws_sdk_bedrock_agent.types.redshift_query_engine_redshift_storage_configuration.serialize_json(
                value["redshift_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> RedshiftQueryEngineStorageConfiguration:
    out: RedshiftQueryEngineStorageConfiguration = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_bedrock_agent.types.redshift_query_engine_storage_type

        out["type"] = (
            aws_sdk_bedrock_agent.types.redshift_query_engine_storage_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError(
            "RedshiftQueryEngineStorageConfiguration.type required"
        )
    if "awsDataCatalogConfiguration" in data:
        import aws_sdk_bedrock_agent.types.redshift_query_engine_aws_data_catalog_storage_configuration

        out["aws_data_catalog_configuration"] = (
            aws_sdk_bedrock_agent.types.redshift_query_engine_aws_data_catalog_storage_configuration.deserialize_json(
                data["awsDataCatalogConfiguration"]
            )
        )
    if "redshiftConfiguration" in data:
        import aws_sdk_bedrock_agent.types.redshift_query_engine_redshift_storage_configuration

        out["redshift_configuration"] = (
            aws_sdk_bedrock_agent.types.redshift_query_engine_redshift_storage_configuration.deserialize_json(
                data["redshiftConfiguration"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.bedrockagent#RedshiftConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.query_generation_configuration
    import aws_sdk_bedrock_agent.types.redshift_query_engine_configuration
    import aws_sdk_bedrock_agent.types.redshift_query_engine_storage_configurations


class RedshiftConfiguration(TypedDict, closed=True):
    storage_configurations: "aws_sdk_bedrock_agent.types.redshift_query_engine_storage_configurations.RedshiftQueryEngineStorageConfigurations"
    """<p>Specifies configurations for Amazon Redshift database storage.</p>"""
    query_engine_configuration: "aws_sdk_bedrock_agent.types.redshift_query_engine_configuration.RedshiftQueryEngineConfiguration"
    """<p>Specifies configurations for an Amazon Redshift query engine.</p>"""
    query_generation_configuration: NotRequired[
        "aws_sdk_bedrock_agent.types.query_generation_configuration.QueryGenerationConfiguration"
    ]
    """<p>Specifies configurations for generating queries.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RedshiftConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.redshift_query_engine_storage_configurations

    out["storageConfigurations"] = (
        aws_sdk_bedrock_agent.types.redshift_query_engine_storage_configurations.serialize_json(
            value["storage_configurations"]
        )
    )
    import aws_sdk_bedrock_agent.types.redshift_query_engine_configuration

    out["queryEngineConfiguration"] = (
        aws_sdk_bedrock_agent.types.redshift_query_engine_configuration.serialize_json(
            value["query_engine_configuration"]
        )
    )
    if "query_generation_configuration" in value:
        import aws_sdk_bedrock_agent.types.query_generation_configuration

        out["queryGenerationConfiguration"] = (
            aws_sdk_bedrock_agent.types.query_generation_configuration.serialize_json(
                value["query_generation_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> RedshiftConfiguration:
    out: RedshiftConfiguration = {}  # type: ignore[typeddict-item]
    if "storageConfigurations" in data:
        import aws_sdk_bedrock_agent.types.redshift_query_engine_storage_configurations

        out["storage_configurations"] = (
            aws_sdk_bedrock_agent.types.redshift_query_engine_storage_configurations.deserialize_json(
                data["storageConfigurations"]
            )
        )
    else:
        raise DeserializationError(
            "RedshiftConfiguration.storage_configurations required"
        )
    if "queryEngineConfiguration" in data:
        import aws_sdk_bedrock_agent.types.redshift_query_engine_configuration

        out["query_engine_configuration"] = (
            aws_sdk_bedrock_agent.types.redshift_query_engine_configuration.deserialize_json(
                data["queryEngineConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "RedshiftConfiguration.query_engine_configuration required"
        )
    if "queryGenerationConfiguration" in data:
        import aws_sdk_bedrock_agent.types.query_generation_configuration

        out["query_generation_configuration"] = (
            aws_sdk_bedrock_agent.types.query_generation_configuration.deserialize_json(
                data["queryGenerationConfiguration"]
            )
        )
    return out

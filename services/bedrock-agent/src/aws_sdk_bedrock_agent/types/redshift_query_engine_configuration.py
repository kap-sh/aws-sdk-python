"""Generated from Smithy shape ``com.amazonaws.bedrockagent#RedshiftQueryEngineConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.redshift_provisioned_configuration
    import aws_sdk_bedrock_agent.types.redshift_query_engine_type
    import aws_sdk_bedrock_agent.types.redshift_serverless_configuration


class RedshiftQueryEngineConfiguration(TypedDict, closed=True):
    type: (
        "aws_sdk_bedrock_agent.types.redshift_query_engine_type.RedshiftQueryEngineType"
    )
    """<p>The type of query engine.</p>"""
    serverless_configuration: NotRequired[
        "aws_sdk_bedrock_agent.types.redshift_serverless_configuration.RedshiftServerlessConfiguration"
    ]
    """<p>Specifies configurations for a serverless Amazon Redshift query engine.</p>"""
    provisioned_configuration: NotRequired[
        "aws_sdk_bedrock_agent.types.redshift_provisioned_configuration.RedshiftProvisionedConfiguration"
    ]
    """<p>Specifies configurations for a provisioned Amazon Redshift query engine.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RedshiftQueryEngineConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.redshift_query_engine_type

    out["type"] = aws_sdk_bedrock_agent.types.redshift_query_engine_type.serialize_json(
        value["type"]
    )
    if "serverless_configuration" in value:
        import aws_sdk_bedrock_agent.types.redshift_serverless_configuration

        out["serverlessConfiguration"] = (
            aws_sdk_bedrock_agent.types.redshift_serverless_configuration.serialize_json(
                value["serverless_configuration"]
            )
        )
    if "provisioned_configuration" in value:
        import aws_sdk_bedrock_agent.types.redshift_provisioned_configuration

        out["provisionedConfiguration"] = (
            aws_sdk_bedrock_agent.types.redshift_provisioned_configuration.serialize_json(
                value["provisioned_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> RedshiftQueryEngineConfiguration:
    out: RedshiftQueryEngineConfiguration = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_bedrock_agent.types.redshift_query_engine_type

        out["type"] = (
            aws_sdk_bedrock_agent.types.redshift_query_engine_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError("RedshiftQueryEngineConfiguration.type required")
    if "serverlessConfiguration" in data:
        import aws_sdk_bedrock_agent.types.redshift_serverless_configuration

        out["serverless_configuration"] = (
            aws_sdk_bedrock_agent.types.redshift_serverless_configuration.deserialize_json(
                data["serverlessConfiguration"]
            )
        )
    if "provisionedConfiguration" in data:
        import aws_sdk_bedrock_agent.types.redshift_provisioned_configuration

        out["provisioned_configuration"] = (
            aws_sdk_bedrock_agent.types.redshift_provisioned_configuration.deserialize_json(
                data["provisionedConfiguration"]
            )
        )
    return out

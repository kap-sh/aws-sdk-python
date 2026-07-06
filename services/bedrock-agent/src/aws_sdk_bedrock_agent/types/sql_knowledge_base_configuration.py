"""Generated from Smithy shape ``com.amazonaws.bedrockagent#SqlKnowledgeBaseConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.query_engine_type
    import aws_sdk_bedrock_agent.types.redshift_configuration


class SqlKnowledgeBaseConfiguration(TypedDict, closed=True):
    type: "aws_sdk_bedrock_agent.types.query_engine_type.QueryEngineType"
    """<p>The type of SQL database to connect to the knowledge base.</p>"""
    redshift_configuration: NotRequired[
        "aws_sdk_bedrock_agent.types.redshift_configuration.RedshiftConfiguration"
    ]
    """<p>Specifies configurations for a knowledge base connected to an Amazon Redshift database.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SqlKnowledgeBaseConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.query_engine_type

    out["type"] = aws_sdk_bedrock_agent.types.query_engine_type.serialize_json(
        value["type"]
    )
    if "redshift_configuration" in value:
        import aws_sdk_bedrock_agent.types.redshift_configuration

        out["redshiftConfiguration"] = (
            aws_sdk_bedrock_agent.types.redshift_configuration.serialize_json(
                value["redshift_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> SqlKnowledgeBaseConfiguration:
    out: SqlKnowledgeBaseConfiguration = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_bedrock_agent.types.query_engine_type

        out["type"] = aws_sdk_bedrock_agent.types.query_engine_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("SqlKnowledgeBaseConfiguration.type required")
    if "redshiftConfiguration" in data:
        import aws_sdk_bedrock_agent.types.redshift_configuration

        out["redshift_configuration"] = (
            aws_sdk_bedrock_agent.types.redshift_configuration.deserialize_json(
                data["redshiftConfiguration"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#TextToSqlConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.text_to_sql_configuration_type
    import aws_sdk_bedrock_agent_runtime.types.text_to_sql_knowledge_base_configuration


class TextToSqlConfiguration(TypedDict, closed=True):
    type: "aws_sdk_bedrock_agent_runtime.types.text_to_sql_configuration_type.TextToSqlConfigurationType"
    """<p>The type of resource to use in transformation.</p>"""
    knowledge_base_configuration: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.text_to_sql_knowledge_base_configuration.TextToSqlKnowledgeBaseConfiguration"
    ]
    """<p>Specifies configurations for a knowledge base to use in transformation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TextToSqlConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent_runtime.types.text_to_sql_configuration_type

    out["type"] = (
        aws_sdk_bedrock_agent_runtime.types.text_to_sql_configuration_type.serialize_json(
            value["type"]
        )
    )
    if "knowledge_base_configuration" in value:
        import aws_sdk_bedrock_agent_runtime.types.text_to_sql_knowledge_base_configuration

        out["knowledgeBaseConfiguration"] = (
            aws_sdk_bedrock_agent_runtime.types.text_to_sql_knowledge_base_configuration.serialize_json(
                value["knowledge_base_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> TextToSqlConfiguration:
    out: TextToSqlConfiguration = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_bedrock_agent_runtime.types.text_to_sql_configuration_type

        out["type"] = (
            aws_sdk_bedrock_agent_runtime.types.text_to_sql_configuration_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError("TextToSqlConfiguration.type required")
    if "knowledgeBaseConfiguration" in data:
        import aws_sdk_bedrock_agent_runtime.types.text_to_sql_knowledge_base_configuration

        out["knowledge_base_configuration"] = (
            aws_sdk_bedrock_agent_runtime.types.text_to_sql_knowledge_base_configuration.deserialize_json(
                data["knowledgeBaseConfiguration"]
            )
        )
    return out

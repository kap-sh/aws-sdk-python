"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#TextToSqlKnowledgeBaseConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.knowledge_base_arn


class TextToSqlKnowledgeBaseConfiguration(TypedDict):
    knowledge_base_arn: (
        "aws_sdk_bedrock_agent_runtime.types.knowledge_base_arn.KnowledgeBaseArn"
    )
    """<p>The ARN of the knowledge base</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TextToSqlKnowledgeBaseConfiguration) -> dict:
    out: dict = {}
    out["knowledgeBaseArn"] = value["knowledge_base_arn"]
    return out


def deserialize_json(data: dict) -> TextToSqlKnowledgeBaseConfiguration:
    out: TextToSqlKnowledgeBaseConfiguration = {}  # type: ignore[typeddict-item]
    if "knowledgeBaseArn" in data:
        out["knowledge_base_arn"] = data["knowledgeBaseArn"]
    else:
        raise DeserializationError(
            "TextToSqlKnowledgeBaseConfiguration.knowledge_base_arn required"
        )
    return out

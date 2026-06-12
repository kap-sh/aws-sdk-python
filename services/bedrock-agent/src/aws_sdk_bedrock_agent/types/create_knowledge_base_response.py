"""Generated from Smithy shape ``com.amazonaws.bedrockagent#CreateKnowledgeBaseResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.knowledge_base


class CreateKnowledgeBaseResponse(TypedDict):
    knowledge_base: "aws_sdk_bedrock_agent.types.knowledge_base.KnowledgeBase"
    """<p>Contains details about the knowledge base.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateKnowledgeBaseResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.knowledge_base

    out["knowledgeBase"] = aws_sdk_bedrock_agent.types.knowledge_base.serialize_json(
        value["knowledge_base"]
    )
    return out


def deserialize_json(data: dict) -> CreateKnowledgeBaseResponse:
    out: CreateKnowledgeBaseResponse = {}  # type: ignore[typeddict-item]
    if "knowledgeBase" in data:
        import aws_sdk_bedrock_agent.types.knowledge_base

        out["knowledge_base"] = (
            aws_sdk_bedrock_agent.types.knowledge_base.deserialize_json(
                data["knowledgeBase"]
            )
        )
    else:
        raise DeserializationError(
            "CreateKnowledgeBaseResponse.knowledge_base required"
        )
    return out

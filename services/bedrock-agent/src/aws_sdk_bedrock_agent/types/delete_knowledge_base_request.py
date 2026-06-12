"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DeleteKnowledgeBaseRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.id


class DeleteKnowledgeBaseRequest(TypedDict):
    knowledge_base_id: "aws_sdk_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the knowledge base to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteKnowledgeBaseRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteKnowledgeBaseRequest:
    out: DeleteKnowledgeBaseRequest = {}  # type: ignore[typeddict-item]
    return out

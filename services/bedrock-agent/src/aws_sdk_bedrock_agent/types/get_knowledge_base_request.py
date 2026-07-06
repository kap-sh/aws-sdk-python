"""Generated from Smithy shape ``com.amazonaws.bedrockagent#GetKnowledgeBaseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.id


class GetKnowledgeBaseRequest(TypedDict, closed=True):
    knowledge_base_id: "aws_sdk_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the knowledge base you want to get information on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetKnowledgeBaseRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetKnowledgeBaseRequest:
    out: GetKnowledgeBaseRequest = {}  # type: ignore[typeddict-item]
    return out

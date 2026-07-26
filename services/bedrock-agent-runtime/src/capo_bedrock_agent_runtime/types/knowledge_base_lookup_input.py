"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#KnowledgeBaseLookupInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.knowledge_base_lookup_input_string
    import capo_bedrock_agent_runtime.types.trace_knowledge_base_id


class KnowledgeBaseLookupInput(TypedDict, closed=True):
    text: NotRequired[
        "capo_bedrock_agent_runtime.types.knowledge_base_lookup_input_string.KnowledgeBaseLookupInputString"
    ]
    """<p>The query made to the knowledge base.</p>"""
    knowledge_base_id: NotRequired[
        "capo_bedrock_agent_runtime.types.trace_knowledge_base_id.TraceKnowledgeBaseId"
    ]
    """<p>The unique identifier of the knowledge base to look up.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseLookupInput) -> dict:
    out: dict = {}
    if "text" in value:
        out["text"] = value["text"]
    if "knowledge_base_id" in value:
        out["knowledgeBaseId"] = value["knowledge_base_id"]
    return out


def deserialize_json(data: dict) -> KnowledgeBaseLookupInput:
    out: KnowledgeBaseLookupInput = {}  # type: ignore[typeddict-item]
    if "text" in data:
        out["text"] = data["text"]
    if "knowledgeBaseId" in data:
        out["knowledge_base_id"] = data["knowledgeBaseId"]
    return out

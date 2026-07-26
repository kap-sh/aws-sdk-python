"""Generated from Smithy shape ``com.amazonaws.bedrockagent#KnowledgeBaseSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.date_timestamp
    import capo_bedrock_agent.types.description
    import capo_bedrock_agent.types.id
    import capo_bedrock_agent.types.knowledge_base_status
    import capo_bedrock_agent.types.name


class KnowledgeBaseSummary(TypedDict, closed=True):
    knowledge_base_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the knowledge base.</p>"""
    name: "capo_bedrock_agent.types.name.Name"
    """<p>The name of the knowledge base.</p>"""
    description: NotRequired["capo_bedrock_agent.types.description.Description"]
    """<p>The description of the knowledge base.</p>"""
    status: "capo_bedrock_agent.types.knowledge_base_status.KnowledgeBaseStatus"
    """<p>The status of the knowledge base.</p>"""
    updated_at: "capo_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time the knowledge base was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseSummary) -> dict:
    out: dict = {}
    out["knowledgeBaseId"] = value["knowledge_base_id"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_bedrock_agent.types.knowledge_base_status

    out["status"] = capo_bedrock_agent.types.knowledge_base_status.serialize_json(
        value["status"]
    )
    import capo_bedrock_agent.types.date_timestamp

    out["updatedAt"] = capo_bedrock_agent.types.date_timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> KnowledgeBaseSummary:
    out: KnowledgeBaseSummary = {}  # type: ignore[typeddict-item]
    if "knowledgeBaseId" in data:
        out["knowledge_base_id"] = data["knowledgeBaseId"]
    else:
        raise DeserializationError("KnowledgeBaseSummary.knowledge_base_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("KnowledgeBaseSummary.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "status" in data:
        import capo_bedrock_agent.types.knowledge_base_status

        out["status"] = capo_bedrock_agent.types.knowledge_base_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("KnowledgeBaseSummary.status required")
    if "updatedAt" in data:
        import capo_bedrock_agent.types.date_timestamp

        out["updated_at"] = capo_bedrock_agent.types.date_timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("KnowledgeBaseSummary.updated_at required")
    return out

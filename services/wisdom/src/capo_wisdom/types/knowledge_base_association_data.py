"""Generated from Smithy shape ``com.amazonaws.wisdom#KnowledgeBaseAssociationData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wisdom.types.arn
    import capo_wisdom.types.uuid


class KnowledgeBaseAssociationData(TypedDict, closed=True):
    knowledge_base_id: NotRequired["capo_wisdom.types.uuid.Uuid"]
    """<p>The identifier of the knowledge base. This should not be a QUICK_RESPONSES type knowledge base if you're storing Wisdom Content resource to it.</p>"""
    knowledge_base_arn: NotRequired["capo_wisdom.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the knowledge base.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseAssociationData) -> dict:
    out: dict = {}
    if "knowledge_base_id" in value:
        out["knowledgeBaseId"] = value["knowledge_base_id"]
    if "knowledge_base_arn" in value:
        out["knowledgeBaseArn"] = value["knowledge_base_arn"]
    return out


def deserialize_json(data: dict) -> KnowledgeBaseAssociationData:
    out: KnowledgeBaseAssociationData = {}  # type: ignore[typeddict-item]
    if "knowledgeBaseId" in data:
        out["knowledge_base_id"] = data["knowledgeBaseId"]
    if "knowledgeBaseArn" in data:
        out["knowledge_base_arn"] = data["knowledgeBaseArn"]
    return out

"""Generated from Smithy shape ``com.amazonaws.qconnect#KnowledgeBaseAssociationData``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.arn
    import aws_sdk_qconnect.types.uuid


class KnowledgeBaseAssociationData(TypedDict):
    knowledge_base_id: NotRequired["aws_sdk_qconnect.types.uuid.Uuid"]
    """<p>The identifier of the knowledge base.</p>"""
    knowledge_base_arn: NotRequired["aws_sdk_qconnect.types.arn.Arn"]
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

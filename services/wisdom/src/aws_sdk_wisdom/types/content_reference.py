"""Generated from Smithy shape ``com.amazonaws.wisdom#ContentReference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wisdom.types.arn
    import aws_sdk_wisdom.types.uuid


class ContentReference(TypedDict, closed=True):
    knowledge_base_arn: NotRequired["aws_sdk_wisdom.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the knowledge base.</p>"""
    knowledge_base_id: NotRequired["aws_sdk_wisdom.types.uuid.Uuid"]
    """<p>The identifier of the knowledge base. This should not be a QUICK_RESPONSES type knowledge base if you're storing Wisdom Content resource to it.</p>"""
    content_arn: NotRequired["aws_sdk_wisdom.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the content.</p>"""
    content_id: NotRequired["aws_sdk_wisdom.types.uuid.Uuid"]
    """<p>The identifier of the content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContentReference) -> dict:
    out: dict = {}
    if "knowledge_base_arn" in value:
        out["knowledgeBaseArn"] = value["knowledge_base_arn"]
    if "knowledge_base_id" in value:
        out["knowledgeBaseId"] = value["knowledge_base_id"]
    if "content_arn" in value:
        out["contentArn"] = value["content_arn"]
    if "content_id" in value:
        out["contentId"] = value["content_id"]
    return out


def deserialize_json(data: dict) -> ContentReference:
    out: ContentReference = {}  # type: ignore[typeddict-item]
    if "knowledgeBaseArn" in data:
        out["knowledge_base_arn"] = data["knowledgeBaseArn"]
    if "knowledgeBaseId" in data:
        out["knowledge_base_id"] = data["knowledgeBaseId"]
    if "contentArn" in data:
        out["content_arn"] = data["contentArn"]
    if "contentId" in data:
        out["content_id"] = data["contentId"]
    return out

"""Generated from Smithy shape ``com.amazonaws.qconnect#SpanCitation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.arn
    import aws_sdk_qconnect.types.sensitive_string
    import aws_sdk_qconnect.types.uuid


class SpanCitation(TypedDict, closed=True):
    content_id: NotRequired["aws_sdk_qconnect.types.uuid.Uuid"]
    """<p>The identifier of the content being cited in the span.</p>"""
    title: NotRequired["aws_sdk_qconnect.types.sensitive_string.SensitiveString"]
    """<p>The title of the content being cited in the span.</p>"""
    knowledge_base_id: NotRequired["aws_sdk_qconnect.types.uuid.Uuid"]
    """<p>The identifier of the knowledge base containing the cited content.</p>"""
    knowledge_base_arn: NotRequired["aws_sdk_qconnect.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the knowledge base containing the cited content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SpanCitation) -> dict:
    out: dict = {}
    if "content_id" in value:
        out["contentId"] = value["content_id"]
    if "title" in value:
        out["title"] = value["title"]
    if "knowledge_base_id" in value:
        out["knowledgeBaseId"] = value["knowledge_base_id"]
    if "knowledge_base_arn" in value:
        out["knowledgeBaseArn"] = value["knowledge_base_arn"]
    return out


def deserialize_json(data: dict) -> SpanCitation:
    out: SpanCitation = {}  # type: ignore[typeddict-item]
    if "contentId" in data:
        out["content_id"] = data["contentId"]
    if "title" in data:
        out["title"] = data["title"]
    if "knowledgeBaseId" in data:
        out["knowledge_base_id"] = data["knowledgeBaseId"]
    if "knowledgeBaseArn" in data:
        out["knowledge_base_arn"] = data["knowledgeBaseArn"]
    return out

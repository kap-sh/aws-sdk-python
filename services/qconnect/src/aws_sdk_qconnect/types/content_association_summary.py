"""Generated from Smithy shape ``com.amazonaws.qconnect#ContentAssociationSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.arn
    import aws_sdk_qconnect.types.content_association_contents
    import aws_sdk_qconnect.types.content_association_type
    import aws_sdk_qconnect.types.tags
    import aws_sdk_qconnect.types.uuid


class ContentAssociationSummary(TypedDict):
    knowledge_base_id: "aws_sdk_qconnect.types.uuid.Uuid"
    """<p>The identifier of the knowledge base.</p>"""
    knowledge_base_arn: "aws_sdk_qconnect.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the knowledge base.</p>"""
    content_id: "aws_sdk_qconnect.types.uuid.Uuid"
    """<p>The identifier of the content.</p>"""
    content_arn: "aws_sdk_qconnect.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the content.</p>"""
    content_association_id: "aws_sdk_qconnect.types.uuid.Uuid"
    """<p>The identifier of the content association. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    content_association_arn: "aws_sdk_qconnect.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the content association.</p>"""
    association_type: (
        "aws_sdk_qconnect.types.content_association_type.ContentAssociationType"
    )
    """<p>The type of association.</p>"""
    association_data: (
        "aws_sdk_qconnect.types.content_association_contents.ContentAssociationContents"
    )
    """<p>The content association.</p>"""
    tags: NotRequired["aws_sdk_qconnect.types.tags.Tags"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContentAssociationSummary) -> dict:
    out: dict = {}
    out["knowledgeBaseId"] = value["knowledge_base_id"]
    out["knowledgeBaseArn"] = value["knowledge_base_arn"]
    out["contentId"] = value["content_id"]
    out["contentArn"] = value["content_arn"]
    out["contentAssociationId"] = value["content_association_id"]
    out["contentAssociationArn"] = value["content_association_arn"]
    out["associationType"] = value["association_type"]
    import aws_sdk_qconnect.types.content_association_contents

    out["associationData"] = (
        aws_sdk_qconnect.types.content_association_contents.serialize_json(
            value["association_data"]
        )
    )
    if "tags" in value:
        import aws_sdk_qconnect.types.tags

        out["tags"] = aws_sdk_qconnect.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ContentAssociationSummary:
    out: ContentAssociationSummary = {}  # type: ignore[typeddict-item]
    if "knowledgeBaseId" in data:
        out["knowledge_base_id"] = data["knowledgeBaseId"]
    else:
        raise DeserializationError(
            "ContentAssociationSummary.knowledge_base_id required"
        )
    if "knowledgeBaseArn" in data:
        out["knowledge_base_arn"] = data["knowledgeBaseArn"]
    else:
        raise DeserializationError(
            "ContentAssociationSummary.knowledge_base_arn required"
        )
    if "contentId" in data:
        out["content_id"] = data["contentId"]
    else:
        raise DeserializationError("ContentAssociationSummary.content_id required")
    if "contentArn" in data:
        out["content_arn"] = data["contentArn"]
    else:
        raise DeserializationError("ContentAssociationSummary.content_arn required")
    if "contentAssociationId" in data:
        out["content_association_id"] = data["contentAssociationId"]
    else:
        raise DeserializationError(
            "ContentAssociationSummary.content_association_id required"
        )
    if "contentAssociationArn" in data:
        out["content_association_arn"] = data["contentAssociationArn"]
    else:
        raise DeserializationError(
            "ContentAssociationSummary.content_association_arn required"
        )
    if "associationType" in data:
        out["association_type"] = data["associationType"]
    else:
        raise DeserializationError(
            "ContentAssociationSummary.association_type required"
        )
    if "associationData" in data:
        import aws_sdk_qconnect.types.content_association_contents

        out["association_data"] = (
            aws_sdk_qconnect.types.content_association_contents.deserialize_json(
                data["associationData"]
            )
        )
    else:
        raise DeserializationError(
            "ContentAssociationSummary.association_data required"
        )
    if "tags" in data:
        import aws_sdk_qconnect.types.tags

        out["tags"] = aws_sdk_qconnect.types.tags.deserialize_json(data["tags"])
    return out

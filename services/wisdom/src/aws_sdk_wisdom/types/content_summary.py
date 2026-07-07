"""Generated from Smithy shape ``com.amazonaws.wisdom#ContentSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_wisdom.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wisdom.types.arn
    import aws_sdk_wisdom.types.content_metadata
    import aws_sdk_wisdom.types.content_status
    import aws_sdk_wisdom.types.content_title
    import aws_sdk_wisdom.types.content_type
    import aws_sdk_wisdom.types.name
    import aws_sdk_wisdom.types.non_empty_string
    import aws_sdk_wisdom.types.tags
    import aws_sdk_wisdom.types.uuid


class ContentSummary(TypedDict, closed=True):
    content_arn: "aws_sdk_wisdom.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the content.</p>"""
    content_id: "aws_sdk_wisdom.types.uuid.Uuid"
    """<p>The identifier of the content.</p>"""
    knowledge_base_arn: "aws_sdk_wisdom.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the knowledge base.</p>"""
    knowledge_base_id: "aws_sdk_wisdom.types.uuid.Uuid"
    """<p>The identifier of the knowledge base. This should not be a QUICK_RESPONSES type knowledge base if you're storing Wisdom Content resource to it.</p>"""
    name: "aws_sdk_wisdom.types.name.Name"
    """<p>The name of the content.</p>"""
    revision_id: "aws_sdk_wisdom.types.non_empty_string.NonEmptyString"
    """<p>The identifier of the revision of the content.</p>"""
    title: "aws_sdk_wisdom.types.content_title.ContentTitle"
    """<p>The title of the content.</p>"""
    content_type: "aws_sdk_wisdom.types.content_type.ContentType"
    """<p>The media type of the content.</p>"""
    status: "aws_sdk_wisdom.types.content_status.ContentStatus"
    """<p>The status of the content.</p>"""
    metadata: "aws_sdk_wisdom.types.content_metadata.ContentMetadata"
    """<p>A key/value map to store attributes without affecting tagging or recommendations. For example, when synchronizing data between an external system and Wisdom, you can store an external version identifier as metadata to utilize for determining drift.</p>"""
    tags: NotRequired["aws_sdk_wisdom.types.tags.Tags"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContentSummary) -> dict:
    out: dict = {}
    out["contentArn"] = value["content_arn"]
    out["contentId"] = value["content_id"]
    out["knowledgeBaseArn"] = value["knowledge_base_arn"]
    out["knowledgeBaseId"] = value["knowledge_base_id"]
    out["name"] = value["name"]
    out["revisionId"] = value["revision_id"]
    out["title"] = value["title"]
    out["contentType"] = value["content_type"]
    out["status"] = value["status"]
    import aws_sdk_wisdom.types.content_metadata

    out["metadata"] = aws_sdk_wisdom.types.content_metadata.serialize_json(
        value["metadata"]
    )
    if "tags" in value:
        import aws_sdk_wisdom.types.tags

        out["tags"] = aws_sdk_wisdom.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ContentSummary:
    out: ContentSummary = {}  # type: ignore[typeddict-item]
    if "contentArn" in data:
        out["content_arn"] = data["contentArn"]
    else:
        raise DeserializationError("ContentSummary.content_arn required")
    if "contentId" in data:
        out["content_id"] = data["contentId"]
    else:
        raise DeserializationError("ContentSummary.content_id required")
    if "knowledgeBaseArn" in data:
        out["knowledge_base_arn"] = data["knowledgeBaseArn"]
    else:
        raise DeserializationError("ContentSummary.knowledge_base_arn required")
    if "knowledgeBaseId" in data:
        out["knowledge_base_id"] = data["knowledgeBaseId"]
    else:
        raise DeserializationError("ContentSummary.knowledge_base_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ContentSummary.name required")
    if "revisionId" in data:
        out["revision_id"] = data["revisionId"]
    else:
        raise DeserializationError("ContentSummary.revision_id required")
    if "title" in data:
        out["title"] = data["title"]
    else:
        raise DeserializationError("ContentSummary.title required")
    if "contentType" in data:
        out["content_type"] = data["contentType"]
    else:
        raise DeserializationError("ContentSummary.content_type required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("ContentSummary.status required")
    if "metadata" in data:
        import aws_sdk_wisdom.types.content_metadata

        out["metadata"] = aws_sdk_wisdom.types.content_metadata.deserialize_json(
            data["metadata"]
        )
    else:
        raise DeserializationError("ContentSummary.metadata required")
    if "tags" in data:
        import aws_sdk_wisdom.types.tags

        out["tags"] = aws_sdk_wisdom.types.tags.deserialize_json(data["tags"])
    return out

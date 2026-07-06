"""Generated from Smithy shape ``com.amazonaws.qconnect#ContentData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_qconnect.types.arn
    import aws_sdk_qconnect.types.content_metadata
    import aws_sdk_qconnect.types.content_status
    import aws_sdk_qconnect.types.content_title
    import aws_sdk_qconnect.types.content_type
    import aws_sdk_qconnect.types.name
    import aws_sdk_qconnect.types.non_empty_string
    import aws_sdk_qconnect.types.tags
    import aws_sdk_qconnect.types.uri
    import aws_sdk_qconnect.types.url
    import aws_sdk_qconnect.types.uuid


class ContentData(TypedDict, closed=True):
    content_arn: "aws_sdk_qconnect.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the content.</p>"""
    content_id: "aws_sdk_qconnect.types.uuid.Uuid"
    """<p>The identifier of the content.</p>"""
    knowledge_base_arn: "aws_sdk_qconnect.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the knowledge base.</p>"""
    knowledge_base_id: "aws_sdk_qconnect.types.uuid.Uuid"
    """<p>The identifier of the knowledge base.</p>"""
    name: "aws_sdk_qconnect.types.name.Name"
    """<p>The name of the content.</p>"""
    revision_id: "aws_sdk_qconnect.types.non_empty_string.NonEmptyString"
    """<p>The identifier of the content revision.</p>"""
    title: "aws_sdk_qconnect.types.content_title.ContentTitle"
    """<p>The title of the content.</p>"""
    content_type: "aws_sdk_qconnect.types.content_type.ContentType"
    """<p>The media type of the content.</p>"""
    status: "aws_sdk_qconnect.types.content_status.ContentStatus"
    """<p>The status of the content.</p>"""
    metadata: "aws_sdk_qconnect.types.content_metadata.ContentMetadata"
    """<p>A key/value map to store attributes without affecting tagging or recommendations. For example, when synchronizing data between an external system and Amazon Q in Connect, you can store an external version identifier as metadata to utilize for determining drift.</p>"""
    tags: NotRequired["aws_sdk_qconnect.types.tags.Tags"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""
    link_out_uri: NotRequired["aws_sdk_qconnect.types.uri.Uri"]
    """<p>The URI of the content.</p>"""
    url: "aws_sdk_qconnect.types.url.Url"
    """<p>The URL of the content.</p>"""
    url_expiry: "datetime.datetime"
    """<p>The expiration time of the URL as an epoch timestamp.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContentData) -> dict:
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
    import aws_sdk_qconnect.types.content_metadata

    out["metadata"] = aws_sdk_qconnect.types.content_metadata.serialize_json(
        value["metadata"]
    )
    if "tags" in value:
        import aws_sdk_qconnect.types.tags

        out["tags"] = aws_sdk_qconnect.types.tags.serialize_json(value["tags"])
    if "link_out_uri" in value:
        out["linkOutUri"] = value["link_out_uri"]
    out["url"] = value["url"]
    import aws_sdk_qconnect.types._prelude.timestamp

    out["urlExpiry"] = aws_sdk_qconnect.types._prelude.timestamp.serialize_json(
        value["url_expiry"]
    )
    return out


def deserialize_json(data: dict) -> ContentData:
    out: ContentData = {}  # type: ignore[typeddict-item]
    if "contentArn" in data:
        out["content_arn"] = data["contentArn"]
    else:
        raise DeserializationError("ContentData.content_arn required")
    if "contentId" in data:
        out["content_id"] = data["contentId"]
    else:
        raise DeserializationError("ContentData.content_id required")
    if "knowledgeBaseArn" in data:
        out["knowledge_base_arn"] = data["knowledgeBaseArn"]
    else:
        raise DeserializationError("ContentData.knowledge_base_arn required")
    if "knowledgeBaseId" in data:
        out["knowledge_base_id"] = data["knowledgeBaseId"]
    else:
        raise DeserializationError("ContentData.knowledge_base_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ContentData.name required")
    if "revisionId" in data:
        out["revision_id"] = data["revisionId"]
    else:
        raise DeserializationError("ContentData.revision_id required")
    if "title" in data:
        out["title"] = data["title"]
    else:
        raise DeserializationError("ContentData.title required")
    if "contentType" in data:
        out["content_type"] = data["contentType"]
    else:
        raise DeserializationError("ContentData.content_type required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("ContentData.status required")
    if "metadata" in data:
        import aws_sdk_qconnect.types.content_metadata

        out["metadata"] = aws_sdk_qconnect.types.content_metadata.deserialize_json(
            data["metadata"]
        )
    else:
        raise DeserializationError("ContentData.metadata required")
    if "tags" in data:
        import aws_sdk_qconnect.types.tags

        out["tags"] = aws_sdk_qconnect.types.tags.deserialize_json(data["tags"])
    if "linkOutUri" in data:
        out["link_out_uri"] = data["linkOutUri"]
    if "url" in data:
        out["url"] = data["url"]
    else:
        raise DeserializationError("ContentData.url required")
    if "urlExpiry" in data:
        import aws_sdk_qconnect.types._prelude.timestamp

        out["url_expiry"] = aws_sdk_qconnect.types._prelude.timestamp.deserialize_json(
            data["urlExpiry"]
        )
    else:
        raise DeserializationError("ContentData.url_expiry required")
    return out

"""Generated from Smithy shape ``com.amazonaws.qconnect#QuickResponseSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_qconnect.types.arn
    import aws_sdk_qconnect.types.channels
    import aws_sdk_qconnect.types.generic_arn
    import aws_sdk_qconnect.types.quick_response_description
    import aws_sdk_qconnect.types.quick_response_name
    import aws_sdk_qconnect.types.quick_response_status
    import aws_sdk_qconnect.types.quick_response_type
    import aws_sdk_qconnect.types.tags
    import aws_sdk_qconnect.types.uuid


class QuickResponseSummary(TypedDict):
    quick_response_arn: "aws_sdk_qconnect.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the quick response.</p>"""
    quick_response_id: "aws_sdk_qconnect.types.uuid.Uuid"
    """<p>The identifier of the quick response.</p>"""
    knowledge_base_arn: "aws_sdk_qconnect.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the knowledge base.</p>"""
    knowledge_base_id: "aws_sdk_qconnect.types.uuid.Uuid"
    """<p>The identifier of the knowledge base.</p>"""
    name: "aws_sdk_qconnect.types.quick_response_name.QuickResponseName"
    """<p>The name of the quick response.</p>"""
    content_type: "aws_sdk_qconnect.types.quick_response_type.QuickResponseType"
    """<p>The media type of the quick response content.</p> <ul> <li> <p>Use <code>application/x.quickresponse;format=plain</code> for quick response written in plain text.</p> </li> <li> <p>Use <code>application/x.quickresponse;format=markdown</code> for quick response written in richtext.</p> </li> </ul>"""
    status: "aws_sdk_qconnect.types.quick_response_status.QuickResponseStatus"
    """<p>The resource status of the quick response.</p>"""
    created_time: "datetime.datetime"
    """<p>The timestamp when the quick response was created.</p>"""
    last_modified_time: "datetime.datetime"
    """<p>The timestamp when the quick response summary was last modified.</p>"""
    description: NotRequired[
        "aws_sdk_qconnect.types.quick_response_description.QuickResponseDescription"
    ]
    """<p>The description of the quick response.</p>"""
    last_modified_by: NotRequired["aws_sdk_qconnect.types.generic_arn.GenericArn"]
    """<p>The Amazon Resource Name (ARN) of the user who last updated the quick response data.</p>"""
    is_active: NotRequired["bool"]
    """<p>Whether the quick response is active.</p>"""
    channels: NotRequired["aws_sdk_qconnect.types.channels.Channels"]
    """<p>The Amazon Connect contact channels this quick response applies to. The supported contact channel types include <code>Chat</code>.</p>"""
    tags: NotRequired["aws_sdk_qconnect.types.tags.Tags"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QuickResponseSummary) -> dict:
    out: dict = {}
    out["quickResponseArn"] = value["quick_response_arn"]
    out["quickResponseId"] = value["quick_response_id"]
    out["knowledgeBaseArn"] = value["knowledge_base_arn"]
    out["knowledgeBaseId"] = value["knowledge_base_id"]
    out["name"] = value["name"]
    out["contentType"] = value["content_type"]
    out["status"] = value["status"]
    import aws_sdk_qconnect.types._prelude.timestamp

    out["createdTime"] = aws_sdk_qconnect.types._prelude.timestamp.serialize_json(
        value["created_time"]
    )
    import aws_sdk_qconnect.types._prelude.timestamp

    out["lastModifiedTime"] = aws_sdk_qconnect.types._prelude.timestamp.serialize_json(
        value["last_modified_time"]
    )
    if "description" in value:
        out["description"] = value["description"]
    if "last_modified_by" in value:
        out["lastModifiedBy"] = value["last_modified_by"]
    if "is_active" in value:
        out["isActive"] = value["is_active"]
    if "channels" in value:
        import aws_sdk_qconnect.types.channels

        out["channels"] = aws_sdk_qconnect.types.channels.serialize_json(
            value["channels"]
        )
    if "tags" in value:
        import aws_sdk_qconnect.types.tags

        out["tags"] = aws_sdk_qconnect.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> QuickResponseSummary:
    out: QuickResponseSummary = {}  # type: ignore[typeddict-item]
    if "quickResponseArn" in data:
        out["quick_response_arn"] = data["quickResponseArn"]
    else:
        raise DeserializationError("QuickResponseSummary.quick_response_arn required")
    if "quickResponseId" in data:
        out["quick_response_id"] = data["quickResponseId"]
    else:
        raise DeserializationError("QuickResponseSummary.quick_response_id required")
    if "knowledgeBaseArn" in data:
        out["knowledge_base_arn"] = data["knowledgeBaseArn"]
    else:
        raise DeserializationError("QuickResponseSummary.knowledge_base_arn required")
    if "knowledgeBaseId" in data:
        out["knowledge_base_id"] = data["knowledgeBaseId"]
    else:
        raise DeserializationError("QuickResponseSummary.knowledge_base_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("QuickResponseSummary.name required")
    if "contentType" in data:
        out["content_type"] = data["contentType"]
    else:
        raise DeserializationError("QuickResponseSummary.content_type required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("QuickResponseSummary.status required")
    if "createdTime" in data:
        import aws_sdk_qconnect.types._prelude.timestamp

        out["created_time"] = (
            aws_sdk_qconnect.types._prelude.timestamp.deserialize_json(
                data["createdTime"]
            )
        )
    else:
        raise DeserializationError("QuickResponseSummary.created_time required")
    if "lastModifiedTime" in data:
        import aws_sdk_qconnect.types._prelude.timestamp

        out["last_modified_time"] = (
            aws_sdk_qconnect.types._prelude.timestamp.deserialize_json(
                data["lastModifiedTime"]
            )
        )
    else:
        raise DeserializationError("QuickResponseSummary.last_modified_time required")
    if "description" in data:
        out["description"] = data["description"]
    if "lastModifiedBy" in data:
        out["last_modified_by"] = data["lastModifiedBy"]
    if "isActive" in data:
        out["is_active"] = data["isActive"]
    if "channels" in data:
        import aws_sdk_qconnect.types.channels

        out["channels"] = aws_sdk_qconnect.types.channels.deserialize_json(
            data["channels"]
        )
    if "tags" in data:
        import aws_sdk_qconnect.types.tags

        out["tags"] = aws_sdk_qconnect.types.tags.deserialize_json(data["tags"])
    return out

"""Generated from Smithy shape ``com.amazonaws.wisdom#QuickResponseSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_wisdom.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_wisdom.types.arn
    import capo_wisdom.types.channels
    import capo_wisdom.types.generic_arn
    import capo_wisdom.types.quick_response_description
    import capo_wisdom.types.quick_response_name
    import capo_wisdom.types.quick_response_status
    import capo_wisdom.types.quick_response_type
    import capo_wisdom.types.tags
    import capo_wisdom.types.uuid


class QuickResponseSummary(TypedDict, closed=True):
    quick_response_arn: "capo_wisdom.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the quick response.</p>"""
    quick_response_id: "capo_wisdom.types.uuid.Uuid"
    """<p>The identifier of the quick response.</p>"""
    knowledge_base_arn: "capo_wisdom.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the knowledge base.</p>"""
    knowledge_base_id: "capo_wisdom.types.uuid.Uuid"
    """<p>The identifier of the knowledge base. This should not be a QUICK_RESPONSES type knowledge base if you're storing Wisdom Content resource to it.</p>"""
    name: "capo_wisdom.types.quick_response_name.QuickResponseName"
    """<p>The name of the quick response.</p>"""
    content_type: "capo_wisdom.types.quick_response_type.QuickResponseType"
    """<p>The media type of the quick response content.</p> <ul> <li> <p>Use <code>application/x.quickresponse;format=plain</code> for quick response written in plain text.</p> </li> <li> <p>Use <code>application/x.quickresponse;format=markdown</code> for quick response written in richtext.</p> </li> </ul>"""
    status: "capo_wisdom.types.quick_response_status.QuickResponseStatus"
    """<p>The resource status of the quick response.</p>"""
    created_time: "datetime.datetime"
    """<p>The timestamp when the quick response was created.</p>"""
    last_modified_time: "datetime.datetime"
    """<p>The timestamp when the quick response summary was last modified.</p>"""
    description: NotRequired[
        "capo_wisdom.types.quick_response_description.QuickResponseDescription"
    ]
    """<p>The description of the quick response.</p>"""
    last_modified_by: NotRequired["capo_wisdom.types.generic_arn.GenericArn"]
    """<p>The Amazon Resource Name (ARN) of the user who last updated the quick response data.</p>"""
    is_active: NotRequired["bool"]
    """<p>Whether the quick response is active.</p>"""
    channels: NotRequired["capo_wisdom.types.channels.Channels"]
    """<p>The Amazon Connect contact channels this quick response applies to. The supported contact channel types include <code>Chat</code>.</p>"""
    tags: NotRequired["capo_wisdom.types.tags.Tags"]
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
    import capo_wisdom.types._prelude.timestamp

    out["createdTime"] = capo_wisdom.types._prelude.timestamp.serialize_json(
        value["created_time"]
    )
    import capo_wisdom.types._prelude.timestamp

    out["lastModifiedTime"] = capo_wisdom.types._prelude.timestamp.serialize_json(
        value["last_modified_time"]
    )
    if "description" in value:
        out["description"] = value["description"]
    if "last_modified_by" in value:
        out["lastModifiedBy"] = value["last_modified_by"]
    if "is_active" in value:
        out["isActive"] = value["is_active"]
    if "channels" in value:
        import capo_wisdom.types.channels

        out["channels"] = capo_wisdom.types.channels.serialize_json(value["channels"])
    if "tags" in value:
        import capo_wisdom.types.tags

        out["tags"] = capo_wisdom.types.tags.serialize_json(value["tags"])
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
        import capo_wisdom.types._prelude.timestamp

        out["created_time"] = capo_wisdom.types._prelude.timestamp.deserialize_json(
            data["createdTime"]
        )
    else:
        raise DeserializationError("QuickResponseSummary.created_time required")
    if "lastModifiedTime" in data:
        import capo_wisdom.types._prelude.timestamp

        out["last_modified_time"] = (
            capo_wisdom.types._prelude.timestamp.deserialize_json(
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
        import capo_wisdom.types.channels

        out["channels"] = capo_wisdom.types.channels.deserialize_json(data["channels"])
    if "tags" in data:
        import capo_wisdom.types.tags

        out["tags"] = capo_wisdom.types.tags.deserialize_json(data["tags"])
    return out

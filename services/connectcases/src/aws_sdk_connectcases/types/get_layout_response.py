"""Generated from Smithy shape ``com.amazonaws.connectcases#GetLayoutResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.created_time
    import aws_sdk_connectcases.types.deleted
    import aws_sdk_connectcases.types.last_modified_time
    import aws_sdk_connectcases.types.layout_arn
    import aws_sdk_connectcases.types.layout_content
    import aws_sdk_connectcases.types.layout_id
    import aws_sdk_connectcases.types.layout_name
    import aws_sdk_connectcases.types.tags


class GetLayoutResponse(TypedDict):
    layout_id: "aws_sdk_connectcases.types.layout_id.LayoutId"
    """<p>The unique identifier of the layout.</p>"""
    layout_arn: "aws_sdk_connectcases.types.layout_arn.LayoutArn"
    """<p>The Amazon Resource Name (ARN) of the newly created layout.</p>"""
    name: "aws_sdk_connectcases.types.layout_name.LayoutName"
    """<p>The name of the layout. It must be unique.</p>"""
    content: "aws_sdk_connectcases.types.layout_content.LayoutContent"
    """<p>Information about which fields will be present in the layout, the order of the fields, and read-only attribute of the field. </p>"""
    tags: NotRequired["aws_sdk_connectcases.types.tags.Tags"]
    """<p>A map of of key-value pairs that represent tags on a resource. Tags are used to organize, track, or control access for this resource.</p>"""
    deleted: "aws_sdk_connectcases.types.deleted.Deleted"
    """<p>Denotes whether or not the resource has been deleted.</p>"""
    created_time: NotRequired["aws_sdk_connectcases.types.created_time.CreatedTime"]
    """<p>Timestamp at which the resource was created.</p>"""
    last_modified_time: NotRequired[
        "aws_sdk_connectcases.types.last_modified_time.LastModifiedTime"
    ]
    """<p>Timestamp at which the resource was created or last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLayoutResponse) -> dict:
    out: dict = {}
    out["layoutId"] = value["layout_id"]
    out["layoutArn"] = value["layout_arn"]
    out["name"] = value["name"]
    import aws_sdk_connectcases.types.layout_content

    out["content"] = aws_sdk_connectcases.types.layout_content.serialize_json(
        value["content"]
    )
    if "tags" in value:
        import aws_sdk_connectcases.types.tags

        out["tags"] = aws_sdk_connectcases.types.tags.serialize_json(value["tags"])
    out["deleted"] = value.get("deleted", False)
    if "created_time" in value:
        import aws_sdk_connectcases.types.created_time

        out["createdTime"] = aws_sdk_connectcases.types.created_time.serialize_json(
            value["created_time"]
        )
    if "last_modified_time" in value:
        import aws_sdk_connectcases.types.last_modified_time

        out["lastModifiedTime"] = (
            aws_sdk_connectcases.types.last_modified_time.serialize_json(
                value["last_modified_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetLayoutResponse:
    out: GetLayoutResponse = {}  # type: ignore[typeddict-item]
    if "layoutId" in data:
        out["layout_id"] = data["layoutId"]
    else:
        raise DeserializationError("GetLayoutResponse.layout_id required")
    if "layoutArn" in data:
        out["layout_arn"] = data["layoutArn"]
    else:
        raise DeserializationError("GetLayoutResponse.layout_arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetLayoutResponse.name required")
    if "content" in data:
        import aws_sdk_connectcases.types.layout_content

        out["content"] = aws_sdk_connectcases.types.layout_content.deserialize_json(
            data["content"]
        )
    else:
        raise DeserializationError("GetLayoutResponse.content required")
    if "tags" in data:
        import aws_sdk_connectcases.types.tags

        out["tags"] = aws_sdk_connectcases.types.tags.deserialize_json(data["tags"])
    if "deleted" in data:
        out["deleted"] = data["deleted"]
    else:
        out["deleted"] = False
    if "createdTime" in data:
        import aws_sdk_connectcases.types.created_time

        out["created_time"] = aws_sdk_connectcases.types.created_time.deserialize_json(
            data["createdTime"]
        )
    if "lastModifiedTime" in data:
        import aws_sdk_connectcases.types.last_modified_time

        out["last_modified_time"] = (
            aws_sdk_connectcases.types.last_modified_time.deserialize_json(
                data["lastModifiedTime"]
            )
        )
    return out

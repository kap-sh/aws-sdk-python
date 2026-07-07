"""Generated from Smithy shape ``com.amazonaws.s3files#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_s3files.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3files.types.resource_id
    import aws_sdk_s3files.types.tag_list


class TagResourceRequest(TypedDict, closed=True):
    resource_id: "aws_sdk_s3files.types.resource_id.ResourceId"
    """<p>The ID or Amazon Resource Name (ARN) of the resource to add tags to.</p>"""
    tags: "aws_sdk_s3files.types.tag_list.TagList"
    """<p>An array of key-value pairs to add as tags to the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_s3files.types.tag_list

    out["tags"] = aws_sdk_s3files.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_s3files.types.tag_list

        out["tags"] = aws_sdk_s3files.types.tag_list.deserialize_json(data["tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out

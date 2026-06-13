"""Generated from Smithy shape ``com.amazonaws.backupsearch#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_backupsearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_backupsearch.types.tag_map


class TagResourceRequest(TypedDict):
    resource_arn: "str"
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the resource.</p> <p>This is the resource that will have the indicated tags.</p>"""
    tags: "aws_sdk_backupsearch.types.tag_map.TagMap"
    """<p>Required tags to include. A tag is a key-value pair you can use to manage, filter, and search for your resources. Allowed characters include UTF-8 letters, numbers, spaces, and the following characters: + - = . _ : /. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_backupsearch.types.tag_map

    out["Tags"] = aws_sdk_backupsearch.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_backupsearch.types.tag_map

        out["tags"] = aws_sdk_backupsearch.types.tag_map.deserialize_json(data["Tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out

"""Generated from Smithy shape ``com.amazonaws.datazone#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.tags


class TagResourceRequest(TypedDict):
    resource_arn: "str"
    """<p>The ARN of the resource to be tagged in Amazon DataZone.</p>"""
    tags: "aws_sdk_datazone.types.tags.Tags"
    """<p>Specifies the tags for the <code>TagResource</code> action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_datazone.types.tags

    out["tags"] = aws_sdk_datazone.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_datazone.types.tags

        out["tags"] = aws_sdk_datazone.types.tags.deserialize_json(data["tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out

"""Generated from Smithy shape ``com.amazonaws.amp#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_amp.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amp.types.tag_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "str"
    """<p>The ARN of the resource to apply tags to.</p>"""
    tags: "aws_sdk_amp.types.tag_map.TagMap"
    """<p>The list of tag keys and values to associate with the resource.</p> <p>Keys must not begin with <code>aws:</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_amp.types.tag_map

    out["tags"] = aws_sdk_amp.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_amp.types.tag_map

        out["tags"] = aws_sdk_amp.types.tag_map.deserialize_json(data["tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out

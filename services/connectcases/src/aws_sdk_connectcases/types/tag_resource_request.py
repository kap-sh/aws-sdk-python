"""Generated from Smithy shape ``com.amazonaws.connectcases#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.arn
    import aws_sdk_connectcases.types.tags


class TagResourceRequest(TypedDict):
    arn: "aws_sdk_connectcases.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN)</p>"""
    tags: "aws_sdk_connectcases.types.tags.Tags"
    """<p>A map of of key-value pairs that represent tags on a resource. Tags are used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_connectcases.types.tags

    out["tags"] = aws_sdk_connectcases.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_connectcases.types.tags

        out["tags"] = aws_sdk_connectcases.types.tags.deserialize_json(data["tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out

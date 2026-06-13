"""Generated from Smithy shape ``com.amazonaws.wisdom#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_wisdom.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wisdom.types.arn
    import aws_sdk_wisdom.types.tags


class TagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_wisdom.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    tags: "aws_sdk_wisdom.types.tags.Tags"
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_wisdom.types.tags

    out["tags"] = aws_sdk_wisdom.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_wisdom.types.tags

        out["tags"] = aws_sdk_wisdom.types.tags.deserialize_json(data["tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out

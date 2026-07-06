"""Generated from Smithy shape ``com.amazonaws.repostspace#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_repostspace.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_repostspace.types.arn
    import aws_sdk_repostspace.types.tags


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_repostspace.types.arn.Arn"
    """<p>The ARN of the resource that the tag is associated with.</p>"""
    tags: "aws_sdk_repostspace.types.tags.Tags"
    """<p>The list of tag keys and values that must be associated with the resource. You can associate tag keys only, tags (key and values) only, or a combination of tag keys and tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_repostspace.types.tags

    out["tags"] = aws_sdk_repostspace.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_repostspace.types.tags

        out["tags"] = aws_sdk_repostspace.types.tags.deserialize_json(data["tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out

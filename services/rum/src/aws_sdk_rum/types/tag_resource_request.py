"""Generated from Smithy shape ``com.amazonaws.rum#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_rum.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rum.types.arn
    import aws_sdk_rum.types.tag_map


class TagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_rum.types.arn.Arn"
    """<p>The ARN of the CloudWatch RUM resource that you're adding tags to.</p>"""
    tags: "aws_sdk_rum.types.tag_map.TagMap"
    """<p>The list of key-value pairs to associate with the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_rum.types.tag_map

    out["Tags"] = aws_sdk_rum.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_rum.types.tag_map

        out["tags"] = aws_sdk_rum.types.tag_map.deserialize_json(data["Tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out

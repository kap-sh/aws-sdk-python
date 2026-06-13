"""Generated from Smithy shape ``com.amazonaws.tnb#TagResourceInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_tnb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_tnb.types.tag_map
    import aws_sdk_tnb.types.tnb_resource_arn


class TagResourceInput(TypedDict):
    resource_arn: "aws_sdk_tnb.types.tnb_resource_arn.TNBResourceArn"
    """<p>Resource ARN.</p>"""
    tags: "aws_sdk_tnb.types.tag_map.TagMap"
    """<p>A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key and an optional value. You can use tags to search and filter your resources or track your Amazon Web Services costs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceInput) -> dict:
    out: dict = {}
    import aws_sdk_tnb.types.tag_map

    out["tags"] = aws_sdk_tnb.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_tnb.types.tag_map

        out["tags"] = aws_sdk_tnb.types.tag_map.deserialize_json(data["tags"])
    else:
        raise DeserializationError("TagResourceInput.tags required")
    return out

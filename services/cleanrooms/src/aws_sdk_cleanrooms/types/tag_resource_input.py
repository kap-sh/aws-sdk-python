"""Generated from Smithy shape ``com.amazonaws.cleanrooms#TagResourceInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.cleanrooms_arn
    import aws_sdk_cleanrooms.types.tag_map


class TagResourceInput(TypedDict):
    resource_arn: "aws_sdk_cleanrooms.types.cleanrooms_arn.CleanroomsArn"
    """<p>The Amazon Resource Name (ARN) associated with the resource you want to tag.</p>"""
    tags: "aws_sdk_cleanrooms.types.tag_map.TagMap"
    """<p>A map of objects specifying each key name and value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceInput) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.tag_map

    out["tags"] = aws_sdk_cleanrooms.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_cleanrooms.types.tag_map

        out["tags"] = aws_sdk_cleanrooms.types.tag_map.deserialize_json(data["tags"])
    else:
        raise DeserializationError("TagResourceInput.tags required")
    return out

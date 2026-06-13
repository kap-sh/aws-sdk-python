"""Generated from Smithy shape ``com.amazonaws.dsql#TagResourceInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_dsql.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dsql.types.arn
    import aws_sdk_dsql.types.tag_map


class TagResourceInput(TypedDict):
    resource_arn: "aws_sdk_dsql.types.arn.Arn"
    """<p>The ARN of the resource that you want to tag.</p>"""
    tags: "aws_sdk_dsql.types.tag_map.TagMap"
    """<p>A map of key and value pairs to use to tag your resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceInput) -> dict:
    out: dict = {}
    import aws_sdk_dsql.types.tag_map

    out["tags"] = aws_sdk_dsql.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_dsql.types.tag_map

        out["tags"] = aws_sdk_dsql.types.tag_map.deserialize_json(data["tags"])
    else:
        raise DeserializationError("TagResourceInput.tags required")
    return out

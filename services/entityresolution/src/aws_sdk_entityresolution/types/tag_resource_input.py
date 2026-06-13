"""Generated from Smithy shape ``com.amazonaws.entityresolution#TagResourceInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_entityresolution.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.tag_map
    import aws_sdk_entityresolution.types.venice_global_arn


class TagResourceInput(TypedDict):
    resource_arn: "aws_sdk_entityresolution.types.venice_global_arn.VeniceGlobalArn"
    """<p>The ARN of the resource for which you want to view tags.</p>"""
    tags: "aws_sdk_entityresolution.types.tag_map.TagMap"
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceInput) -> dict:
    out: dict = {}
    import aws_sdk_entityresolution.types.tag_map

    out["tags"] = aws_sdk_entityresolution.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_entityresolution.types.tag_map

        out["tags"] = aws_sdk_entityresolution.types.tag_map.deserialize_json(
            data["tags"]
        )
    else:
        raise DeserializationError("TagResourceInput.tags required")
    return out

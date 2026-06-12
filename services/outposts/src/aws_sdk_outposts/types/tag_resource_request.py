"""Generated from Smithy shape ``com.amazonaws.outposts#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_outposts.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_outposts.types.arn
    import aws_sdk_outposts.types.tag_map


class TagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_outposts.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    tags: "aws_sdk_outposts.types.tag_map.TagMap"
    """<p>The tags to add to the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_outposts.types.tag_map

    out["Tags"] = aws_sdk_outposts.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_outposts.types.tag_map

        out["tags"] = aws_sdk_outposts.types.tag_map.deserialize_json(data["Tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out

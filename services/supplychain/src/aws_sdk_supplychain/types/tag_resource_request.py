"""Generated from Smithy shape ``com.amazonaws.supplychain#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_supplychain.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_supplychain.types.asc_resource_arn
    import aws_sdk_supplychain.types.tag_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_supplychain.types.asc_resource_arn.AscResourceArn"
    """<p>The Amazon Web Services Supply chain resource ARN that needs to be tagged.</p>"""
    tags: "aws_sdk_supplychain.types.tag_map.TagMap"
    """<p>The tags of the Amazon Web Services Supply chain resource to be created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_supplychain.types.tag_map

    out["tags"] = aws_sdk_supplychain.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_supplychain.types.tag_map

        out["tags"] = aws_sdk_supplychain.types.tag_map.deserialize_json(data["tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out

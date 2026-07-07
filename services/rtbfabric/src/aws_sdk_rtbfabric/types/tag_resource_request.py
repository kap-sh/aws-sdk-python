"""Generated from Smithy shape ``com.amazonaws.rtbfabric#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_rtbfabric.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rtbfabric.types.rtb_taggable_resource_arn
    import aws_sdk_rtbfabric.types.tags_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: (
        "aws_sdk_rtbfabric.types.rtb_taggable_resource_arn.RtbTaggableResourceArn"
    )
    """<p>The Amazon Resource Name (ARN) of the resource that you want to tag.</p>"""
    tags: "aws_sdk_rtbfabric.types.tags_map.TagsMap"
    """<p>A map of the key-value pairs of the tag or tags to assign to the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_rtbfabric.types.tags_map

    out["tags"] = aws_sdk_rtbfabric.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_rtbfabric.types.tags_map

        out["tags"] = aws_sdk_rtbfabric.types.tags_map.deserialize_json(data["tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out

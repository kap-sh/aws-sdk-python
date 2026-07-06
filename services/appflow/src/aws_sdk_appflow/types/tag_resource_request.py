"""Generated from Smithy shape ``com.amazonaws.appflow#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appflow.types.arn
    import aws_sdk_appflow.types.tag_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_appflow.types.arn.ARN"
    """<p> The Amazon Resource Name (ARN) of the flow that you want to tag. </p>"""
    tags: "aws_sdk_appflow.types.tag_map.TagMap"
    """<p> The tags used to organize, track, or control access for your flow. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_appflow.types.tag_map

    out["tags"] = aws_sdk_appflow.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_appflow.types.tag_map

        out["tags"] = aws_sdk_appflow.types.tag_map.deserialize_json(data["tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out

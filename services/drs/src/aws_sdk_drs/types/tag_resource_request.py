"""Generated from Smithy shape ``com.amazonaws.drs#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_drs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_drs.types.arn
    import aws_sdk_drs.types.tags_map


class TagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_drs.types.arn.ARN"
    """<p>ARN of the resource for which tags are to be added or updated.</p>"""
    tags: "aws_sdk_drs.types.tags_map.TagsMap"
    """<p>Array of tags to be added or updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_drs.types.tags_map

    out["tags"] = aws_sdk_drs.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_drs.types.tags_map

        out["tags"] = aws_sdk_drs.types.tags_map.deserialize_json(data["tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out

"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_accessanalyzer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.tags_map


class TagResourceRequest(TypedDict):
    resource_arn: "str"
    """<p>The ARN of the resource to add the tag to.</p>"""
    tags: "aws_sdk_accessanalyzer.types.tags_map.TagsMap"
    """<p>The tags to add to the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_accessanalyzer.types.tags_map

    out["tags"] = aws_sdk_accessanalyzer.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_accessanalyzer.types.tags_map

        out["tags"] = aws_sdk_accessanalyzer.types.tags_map.deserialize_json(
            data["tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out

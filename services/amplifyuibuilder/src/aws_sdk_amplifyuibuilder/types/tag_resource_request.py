"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_amplifyuibuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.tags


class TagResourceRequest(TypedDict):
    resource_arn: "str"
    """<p>The Amazon Resource Name (ARN) to use to tag a resource.</p>"""
    tags: "aws_sdk_amplifyuibuilder.types.tags.Tags"
    """<p>A list of tag key value pairs for a specified Amazon Resource Name (ARN).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_amplifyuibuilder.types.tags

    out["tags"] = aws_sdk_amplifyuibuilder.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_amplifyuibuilder.types.tags

        out["tags"] = aws_sdk_amplifyuibuilder.types.tags.deserialize_json(data["tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out

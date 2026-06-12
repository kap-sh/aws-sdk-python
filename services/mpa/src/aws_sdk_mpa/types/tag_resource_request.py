"""Generated from Smithy shape ``com.amazonaws.mpa#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mpa.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mpa.types.string
    import aws_sdk_mpa.types.tags


class TagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_mpa.types.string.String"
    """<p>Amazon Resource Name (ARN) for the resource you want to tag.</p>"""
    tags: "aws_sdk_mpa.types.tags.Tags"
    """<p>Tags that you have added to the specified resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_mpa.types.tags

    out["Tags"] = aws_sdk_mpa.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_mpa.types.tags

        out["tags"] = aws_sdk_mpa.types.tags.deserialize_json(data["Tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out

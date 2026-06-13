"""Generated from Smithy shape ``com.amazonaws.qbusiness#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.amazon_resource_name
    import aws_sdk_qbusiness.types.tags


class TagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_qbusiness.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the Amazon Q Business application or data source to tag.</p>"""
    tags: "aws_sdk_qbusiness.types.tags.Tags"
    """<p>A list of tag keys to add to the Amazon Q Business application or data source. If a tag already exists, the existing value is replaced with the new value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_qbusiness.types.tags

    out["tags"] = aws_sdk_qbusiness.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_qbusiness.types.tags

        out["tags"] = aws_sdk_qbusiness.types.tags.deserialize_json(data["tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out

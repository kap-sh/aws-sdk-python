"""Generated from Smithy shape ``com.amazonaws.qbusiness#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.amazon_resource_name
    import aws_sdk_qbusiness.types.tag_keys


class UntagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_qbusiness.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the Amazon Q Business application, or data source to remove the tag from.</p>"""
    tag_keys: "aws_sdk_qbusiness.types.tag_keys.TagKeys"
    """<p>A list of tag keys to remove from the Amazon Q Business application or data source. If a tag key does not exist on the resource, it is ignored.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out

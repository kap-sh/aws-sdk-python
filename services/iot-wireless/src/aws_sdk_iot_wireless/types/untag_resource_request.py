"""Generated from Smithy shape ``com.amazonaws.iotwireless#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.amazon_resource_name
    import aws_sdk_iot_wireless.types.tag_key_list


class UntagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_iot_wireless.types.amazon_resource_name.AmazonResourceName"
    """<p>The ARN of the resource to remove tags from.</p>"""
    tag_keys: "aws_sdk_iot_wireless.types.tag_key_list.TagKeyList"
    """<p>A list of the keys of the tags to remove from the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out

"""Generated from Smithy shape ``com.amazonaws.iotevents#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.amazon_resource_name
    import aws_sdk_iot_events.types.tag_keys


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_iot_events.types.amazon_resource_name.AmazonResourceName"
    """<p>The ARN of the resource.</p>"""
    tag_keys: "aws_sdk_iot_events.types.tag_keys.TagKeys"
    """<p>A list of the keys of the tags to be removed from the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out

"""Generated from Smithy shape ``com.amazonaws.iotwireless#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.amazon_resource_name


class ListTagsForResourceRequest(TypedDict):
    resource_arn: "aws_sdk_iot_wireless.types.amazon_resource_name.AmazonResourceName"
    """<p>The ARN of the resource for which you want to list tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out

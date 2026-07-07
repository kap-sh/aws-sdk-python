"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.amazon_resource_name
    import aws_sdk_iotfleetwise.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_iotfleetwise.types.amazon_resource_name.AmazonResourceName"
    """<p>The ARN of the resource.</p>"""
    tag_keys: "aws_sdk_iotfleetwise.types.tag_key_list.TagKeyList"
    """<p>A list of the keys of the tags to be removed from the resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out

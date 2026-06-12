"""Generated from Smithy shape ``com.amazonaws.networkmanager#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.resource_arn
    import aws_sdk_networkmanager.types.tag_key_list


class UntagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_networkmanager.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    tag_keys: "aws_sdk_networkmanager.types.tag_key_list.TagKeyList"
    """<p>The tag keys to remove from the specified resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out

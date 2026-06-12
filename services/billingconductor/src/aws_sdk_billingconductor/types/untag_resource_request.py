"""Generated from Smithy shape ``com.amazonaws.billingconductor#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.arn
    import aws_sdk_billingconductor.types.tag_key_list


class UntagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_billingconductor.types.arn.Arn"
    """<p> The Amazon Resource Name (ARN) of the resource to which to delete tags. </p>"""
    tag_keys: "aws_sdk_billingconductor.types.tag_key_list.TagKeyList"
    """<p> The tags to delete from the resource as a list of key-value pairs. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out

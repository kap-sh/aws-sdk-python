"""Generated from Smithy shape ``com.amazonaws.supplychain#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_supplychain.types.asc_resource_arn
    import aws_sdk_supplychain.types.tag_key_list


class UntagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_supplychain.types.asc_resource_arn.AscResourceArn"
    """<p>The Amazon Web Services Supply chain resource ARN that needs to be untagged.</p>"""
    tag_keys: "aws_sdk_supplychain.types.tag_key_list.TagKeyList"
    """<p>The list of tag keys to be deleted for an Amazon Web Services Supply Chain resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out

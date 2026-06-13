"""Generated from Smithy shape ``com.amazonaws.securitylake#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securitylake.types.amazon_resource_name
    import aws_sdk_securitylake.types.tag_key_list


class UntagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_securitylake.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the Amazon Security Lake resource to remove one or more tags from.</p>"""
    tag_keys: "aws_sdk_securitylake.types.tag_key_list.TagKeyList"
    """<p>A list of one or more tag keys. For each value in the list, specify the tag key for a tag to remove from the Amazon Security Lake resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out

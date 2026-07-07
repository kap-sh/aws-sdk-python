"""Generated from Smithy shape ``com.amazonaws.securityhub#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.resource_arn
    import aws_sdk_securityhub.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_securityhub.types.resource_arn.ResourceArn"
    """<p>The ARN of the resource to remove the tags from.</p>"""
    tag_keys: NotRequired["aws_sdk_securityhub.types.tag_key_list.TagKeyList"]
    """<p>The tag keys associated with the tags to remove from the resource. You can remove up to 50 tags at a time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out

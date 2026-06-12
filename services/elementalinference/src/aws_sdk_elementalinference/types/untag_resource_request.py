"""Generated from Smithy shape ``com.amazonaws.elementalinference#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_elementalinference.types.resource_arn
    import aws_sdk_elementalinference.types.tag_key_list


class UntagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_elementalinference.types.resource_arn.ResourceArn"
    """<p>The ARN of the resource where you want to delete one or more tags.</p>"""
    tag_keys: "aws_sdk_elementalinference.types.tag_key_list.TagKeyList"
    """<p>The keys of the tags to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out

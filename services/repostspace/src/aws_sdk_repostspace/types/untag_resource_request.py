"""Generated from Smithy shape ``com.amazonaws.repostspace#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_repostspace.types.arn
    import aws_sdk_repostspace.types.tag_key_list


class UntagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_repostspace.types.arn.Arn"
    """<p>The ARN of the resource.</p>"""
    tag_keys: "aws_sdk_repostspace.types.tag_key_list.TagKeyList"
    """<p>The key values of the tag.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out

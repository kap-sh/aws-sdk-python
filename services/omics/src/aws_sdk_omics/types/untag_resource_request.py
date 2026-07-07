"""Generated from Smithy shape ``com.amazonaws.omics#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.tag_arn
    import aws_sdk_omics.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_omics.types.tag_arn.TagArn"
    """<p>The resource's ARN.</p>"""
    tag_keys: "aws_sdk_omics.types.tag_key_list.TagKeyList"
    """<p>Keys of tags to remove.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out

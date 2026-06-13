"""Generated from Smithy shape ``com.amazonaws.quicksight#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.tag_key_list


class UntagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_quicksight.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the resource that you want to untag.</p>"""
    tag_keys: "aws_sdk_quicksight.types.tag_key_list.TagKeyList"
    """<p>The keys of the key-value pairs for the resource tag or tags assigned to the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out

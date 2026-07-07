"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.tag_key_list
    import aws_sdk_iottwinmaker.types.twin_maker_arn


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_iottwinmaker.types.twin_maker_arn.TwinMakerArn"
    """<p>The ARN of the resource.</p>"""
    tag_keys: "aws_sdk_iottwinmaker.types.tag_key_list.TagKeyList"
    """<p>A list of tag key names to remove from the resource. You don't specify the value. Both the key and its associated value are removed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out

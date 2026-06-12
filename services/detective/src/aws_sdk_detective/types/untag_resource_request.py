"""Generated from Smithy shape ``com.amazonaws.detective#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_detective.types.graph_arn
    import aws_sdk_detective.types.tag_key_list


class UntagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_detective.types.graph_arn.GraphArn"
    """<p>The ARN of the behavior graph to remove the tags from.</p>"""
    tag_keys: "aws_sdk_detective.types.tag_key_list.TagKeyList"
    """<p>The tag keys of the tags to remove from the behavior graph. You can remove up to 50 tags at a time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out

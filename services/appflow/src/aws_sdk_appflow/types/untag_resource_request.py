"""Generated from Smithy shape ``com.amazonaws.appflow#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appflow.types.arn
    import aws_sdk_appflow.types.tag_key_list


class UntagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_appflow.types.arn.ARN"
    """<p> The Amazon Resource Name (ARN) of the flow that you want to untag. </p>"""
    tag_keys: "aws_sdk_appflow.types.tag_key_list.TagKeyList"
    """<p> The tag keys associated with the tag that you want to remove from your flow. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out

"""Generated from Smithy shape ``com.amazonaws.lambda#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lambda.types.tag_key_list
    import aws_sdk_lambda.types.taggable_resource


class UntagResourceRequest(TypedDict):
    resource: "aws_sdk_lambda.types.taggable_resource.TaggableResource"
    """<p>The resource's Amazon Resource Name (ARN).</p>"""
    tag_keys: "aws_sdk_lambda.types.tag_key_list.TagKeyList"
    """<p>A list of tag keys to remove from the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out

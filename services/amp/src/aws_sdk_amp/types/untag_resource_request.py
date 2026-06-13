"""Generated from Smithy shape ``com.amazonaws.amp#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_amp.types.tag_keys


class UntagResourceRequest(TypedDict):
    resource_arn: "str"
    """<p>The ARN of the resource from which to remove a tag.</p>"""
    tag_keys: "aws_sdk_amp.types.tag_keys.TagKeys"
    """<p>The keys of the tags to remove.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out

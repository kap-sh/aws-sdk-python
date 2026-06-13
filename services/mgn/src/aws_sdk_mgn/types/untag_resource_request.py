"""Generated from Smithy shape ``com.amazonaws.mgn#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mgn.types.arn
    import aws_sdk_mgn.types.tag_keys


class UntagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_mgn.types.arn.ARN"
    """<p>Untag resource by ARN.</p>"""
    tag_keys: "aws_sdk_mgn.types.tag_keys.TagKeys"
    """<p>Untag resource by Keys.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out

"""Generated from Smithy shape ``com.amazonaws.drs#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_drs.types.arn
    import aws_sdk_drs.types.tag_keys


class UntagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_drs.types.arn.ARN"
    """<p>ARN of the resource for which tags are to be removed.</p>"""
    tag_keys: "aws_sdk_drs.types.tag_keys.TagKeys"
    """<p>Array of tags to be removed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out

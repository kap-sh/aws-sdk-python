"""Generated from Smithy shape ``com.amazonaws.groundstation#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.any_arn
    import aws_sdk_groundstation.types.tag_keys


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_groundstation.types.any_arn.AnyArn"
    """<p>ARN of a resource.</p>"""
    tag_keys: "aws_sdk_groundstation.types.tag_keys.TagKeys"
    """<p>Keys of a resource tag.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out

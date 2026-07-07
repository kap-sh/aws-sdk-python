"""Generated from Smithy shape ``com.amazonaws.tnb#UntagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_tnb.types.tag_keys
    import aws_sdk_tnb.types.tnb_resource_arn


class UntagResourceInput(TypedDict, closed=True):
    resource_arn: "aws_sdk_tnb.types.tnb_resource_arn.TNBResourceArn"
    """<p>Resource ARN.</p>"""
    tag_keys: "aws_sdk_tnb.types.tag_keys.TagKeys"
    """<p>Tag keys.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceInput:
    out: UntagResourceInput = {}  # type: ignore[typeddict-item]
    return out

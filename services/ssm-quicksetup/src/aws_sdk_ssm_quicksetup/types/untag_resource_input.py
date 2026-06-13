"""Generated from Smithy shape ``com.amazonaws.ssmquicksetup#UntagResourceInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm_quicksetup.types.tag_keys


class UntagResourceInput(TypedDict):
    resource_arn: "str"
    """<p>The ARN of the resource to remove tags from.</p>"""
    tag_keys: "aws_sdk_ssm_quicksetup.types.tag_keys.TagKeys"
    """<p>The keys of the tags to remove from the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceInput:
    out: UntagResourceInput = {}  # type: ignore[typeddict-item]
    return out

"""Generated from Smithy shape ``com.amazonaws.cleanrooms#UntagResourceInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.cleanrooms_arn
    import aws_sdk_cleanrooms.types.tag_keys


class UntagResourceInput(TypedDict):
    resource_arn: "aws_sdk_cleanrooms.types.cleanrooms_arn.CleanroomsArn"
    """<p>The Amazon Resource Name (ARN) associated with the resource you want to remove the tag from.</p>"""
    tag_keys: "aws_sdk_cleanrooms.types.tag_keys.TagKeys"
    """<p>A list of key names of tags to be removed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceInput:
    out: UntagResourceInput = {}  # type: ignore[typeddict-item]
    return out

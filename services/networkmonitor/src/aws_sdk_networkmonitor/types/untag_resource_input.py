"""Generated from Smithy shape ``com.amazonaws.networkmonitor#UntagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmonitor.types.arn
    import aws_sdk_networkmonitor.types.tag_key_list


class UntagResourceInput(TypedDict, closed=True):
    resource_arn: "aws_sdk_networkmonitor.types.arn.Arn"
    """<p>The ARN of the monitor or probe that the tag should be removed from. </p>"""
    tag_keys: "aws_sdk_networkmonitor.types.tag_key_list.TagKeyList"
    """<p>The key-value pa</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceInput:
    out: UntagResourceInput = {}  # type: ignore[typeddict-item]
    return out

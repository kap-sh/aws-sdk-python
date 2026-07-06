"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#UntagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkflowmonitor.types.arn
    import aws_sdk_networkflowmonitor.types.tag_key_list


class UntagResourceInput(TypedDict, closed=True):
    resource_arn: "aws_sdk_networkflowmonitor.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    tag_keys: "aws_sdk_networkflowmonitor.types.tag_key_list.TagKeyList"
    """<p>Keys that you specified when you tagged a resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceInput:
    out: UntagResourceInput = {}  # type: ignore[typeddict-item]
    return out

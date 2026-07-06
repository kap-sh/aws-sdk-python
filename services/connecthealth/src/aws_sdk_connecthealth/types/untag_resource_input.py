"""Generated from Smithy shape ``com.amazonaws.connecthealth#UntagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_connecthealth.types.tag_key_list


class UntagResourceInput(TypedDict, closed=True):
    resource_arn: "str"
    """<p>The ARN of the resource to untag</p>"""
    tag_keys: "aws_sdk_connecthealth.types.tag_key_list.TagKeyList"
    """<p>The tag keys to remove from the resource</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceInput:
    out: UntagResourceInput = {}  # type: ignore[typeddict-item]
    return out

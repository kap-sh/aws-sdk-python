"""Generated from Smithy shape ``com.amazonaws.securityagent#UntagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.resource_arn
    import aws_sdk_securityagent.types.tag_key_list


class UntagResourceInput(TypedDict, closed=True):
    resource_arn: "aws_sdk_securityagent.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource to remove tags from.</p>"""
    tag_keys: "aws_sdk_securityagent.types.tag_key_list.TagKeyList"
    """<p>The list of tag keys to remove from the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceInput:
    out: UntagResourceInput = {}  # type: ignore[typeddict-item]
    return out

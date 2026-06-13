"""Generated from Smithy shape ``com.amazonaws.ssmincidents#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.tag_key_list


class UntagResourceRequest(TypedDict):
    resource_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the response plan you're removing a tag from.</p>"""
    tag_keys: "aws_sdk_ssm_incidents.types.tag_key_list.TagKeyList"
    """<p>The name of the tag to remove from the response plan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out

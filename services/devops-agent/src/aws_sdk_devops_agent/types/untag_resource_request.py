"""Generated from Smithy shape ``com.amazonaws.devopsagent#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.tag_key_list


class UntagResourceRequest(TypedDict):
    resource_arn: "str"
    """<p>The ARN of the resource to untag.</p>"""
    tag_keys: "aws_sdk_devops_agent.types.tag_key_list.TagKeyList"
    """<p>Tag keys to remove.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out

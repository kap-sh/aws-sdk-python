"""Generated from Smithy shape ``com.amazonaws.workspacesweb#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.arn
    import aws_sdk_workspaces_web.types.tag_key_list


class UntagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the resource.</p>"""
    tag_keys: "aws_sdk_workspaces_web.types.tag_key_list.TagKeyList"
    """<p>The list of tag keys to remove from the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out

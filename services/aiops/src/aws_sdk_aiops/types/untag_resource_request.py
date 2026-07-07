"""Generated from Smithy shape ``com.amazonaws.aiops#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_aiops.types.tag_keys


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the resource that you want to remove the tags from. You can use the<code>ListInvestigationGroups</code> operation to find the ARNs of investigation groups.</p>"""
    tag_keys: "aws_sdk_aiops.types.tag_keys.TagKeys"
    """<p>The list of tag keys to remove from the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out

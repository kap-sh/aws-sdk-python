"""Generated from Smithy shape ``com.amazonaws.efs#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_efs.types.resource_id
    import aws_sdk_efs.types.tag_keys


class UntagResourceRequest(TypedDict, closed=True):
    resource_id: "aws_sdk_efs.types.resource_id.ResourceId"
    """<p>Specifies the EFS resource that you want to remove tags from.</p>"""
    tag_keys: "aws_sdk_efs.types.tag_keys.TagKeys"
    """<p>The keys of the key-value tag pairs that you want to remove from the specified EFS resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out

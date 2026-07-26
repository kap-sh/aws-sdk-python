"""Generated from Smithy shape ``com.amazonaws.s3files#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_s3files.types.resource_id
    import capo_s3files.types.tag_keys


class UntagResourceRequest(TypedDict, closed=True):
    resource_id: "capo_s3files.types.resource_id.ResourceId"
    """<p>The ID or Amazon Resource Name (ARN) of the resource to remove tags from.</p>"""
    tag_keys: "capo_s3files.types.tag_keys.TagKeys"
    """<p>An array of tag keys to remove from the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out

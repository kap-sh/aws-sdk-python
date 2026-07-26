"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.tag_keys
    import capo_cleanroomsml.types.taggable_arn


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_cleanroomsml.types.taggable_arn.TaggableArn"
    """<p>The Amazon Resource Name (ARN) of the resource that you want to remove tags from.</p>"""
    tag_keys: "capo_cleanroomsml.types.tag_keys.TagKeys"
    """<p>The key values of tags that you want to remove.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out

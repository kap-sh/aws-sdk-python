"""Generated from Smithy shape ``com.amazonaws.panorama#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_panorama.types.resource_arn
    import capo_panorama.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_panorama.types.resource_arn.ResourceArn"
    """<p>The resource's ARN.</p>"""
    tag_keys: "capo_panorama.types.tag_key_list.TagKeyList"
    """<p>Tag keys to remove.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out

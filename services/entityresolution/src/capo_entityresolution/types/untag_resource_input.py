"""Generated from Smithy shape ``com.amazonaws.entityresolution#UntagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_entityresolution.types.tag_key_list
    import capo_entityresolution.types.venice_global_arn


class UntagResourceInput(TypedDict, closed=True):
    resource_arn: "capo_entityresolution.types.venice_global_arn.VeniceGlobalArn"
    """<p>The ARN of the resource for which you want to untag.</p>"""
    tag_keys: "capo_entityresolution.types.tag_key_list.TagKeyList"
    """<p>The list of tag keys to remove from the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceInput:
    out: UntagResourceInput = {}  # type: ignore[typeddict-item]
    return out

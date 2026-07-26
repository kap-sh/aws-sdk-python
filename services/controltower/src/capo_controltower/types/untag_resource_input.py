"""Generated from Smithy shape ``com.amazonaws.controltower#UntagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_controltower.types.arn
    import capo_controltower.types.tag_keys


class UntagResourceInput(TypedDict, closed=True):
    resource_arn: "capo_controltower.types.arn.Arn"
    """<p>The ARN of the resource.</p>"""
    tag_keys: "capo_controltower.types.tag_keys.TagKeys"
    """<p>Tag keys to be removed from the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceInput:
    out: UntagResourceInput = {}  # type: ignore[typeddict-item]
    return out

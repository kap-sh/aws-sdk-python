"""Generated from Smithy shape ``com.amazonaws.ssmquicksetup#UntagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm_quicksetup.types.tag_keys


class UntagResourceInput(TypedDict, closed=True):
    resource_arn: "str"
    """<p>The ARN of the resource to remove tags from.</p>"""
    tag_keys: "capo_ssm_quicksetup.types.tag_keys.TagKeys"
    """<p>The keys of the tags to remove from the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceInput:
    out: UntagResourceInput = {}  # type: ignore[typeddict-item]
    return out

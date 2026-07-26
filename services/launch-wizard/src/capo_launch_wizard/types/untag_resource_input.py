"""Generated from Smithy shape ``com.amazonaws.launchwizard#UntagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_launch_wizard.types.tag_key_list


class UntagResourceInput(TypedDict, closed=True):
    resource_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    tag_keys: "capo_launch_wizard.types.tag_key_list.TagKeyList"
    """<p>Keys identifying the tags to remove.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceInput:
    out: UntagResourceInput = {}  # type: ignore[typeddict-item]
    return out

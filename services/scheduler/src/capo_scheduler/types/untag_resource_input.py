"""Generated from Smithy shape ``com.amazonaws.scheduler#UntagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_scheduler.types.tag_key_list
    import capo_scheduler.types.tag_resource_arn


class UntagResourceInput(TypedDict, closed=True):
    resource_arn: "capo_scheduler.types.tag_resource_arn.TagResourceArn"
    """<p>The Amazon Resource Name (ARN) of the schedule group from which you are removing tags.</p>"""
    tag_keys: "capo_scheduler.types.tag_key_list.TagKeyList"
    """<p>The list of tag keys to remove from the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceInput:
    out: UntagResourceInput = {}  # type: ignore[typeddict-item]
    return out

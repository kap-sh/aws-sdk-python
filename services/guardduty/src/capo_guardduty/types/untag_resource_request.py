"""Generated from Smithy shape ``com.amazonaws.guardduty#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.guard_duty_arn
    import capo_guardduty.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_guardduty.types.guard_duty_arn.GuardDutyArn"
    """<p>The Amazon Resource Name (ARN) for the resource to remove tags from.</p>"""
    tag_keys: NotRequired["capo_guardduty.types.tag_key_list.TagKeyList"]
    """<p>The tag keys to remove from the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out

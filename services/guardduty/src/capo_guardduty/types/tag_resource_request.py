"""Generated from Smithy shape ``com.amazonaws.guardduty#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_guardduty.errors import DeserializationError

if TYPE_CHECKING:
    import capo_guardduty.types.guard_duty_arn
    import capo_guardduty.types.tag_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: NotRequired["capo_guardduty.types.guard_duty_arn.GuardDutyArn"]
    """<p>The Amazon Resource Name (ARN) for the GuardDuty resource to apply a tag to.</p>"""
    tags: "capo_guardduty.types.tag_map.TagMap"
    """<p>The tags to be added to a resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_guardduty.types.tag_map

    out["tags"] = capo_guardduty.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import capo_guardduty.types.tag_map

        out["tags"] = capo_guardduty.types.tag_map.deserialize_json(data["tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out

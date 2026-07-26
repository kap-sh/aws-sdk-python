"""Generated from Smithy shape ``com.amazonaws.guardduty#TriggerDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.non_empty_string
    import capo_guardduty.types.trigger_type


class TriggerDetails(TypedDict, closed=True):
    guard_duty_finding_id: NotRequired[
        "capo_guardduty.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ID of the GuardDuty finding that triggered the malware scan.</p>"""
    description: NotRequired["capo_guardduty.types.non_empty_string.NonEmptyString"]
    """<p>The description of the scan trigger.</p>"""
    trigger_type: NotRequired["capo_guardduty.types.trigger_type.TriggerType"]
    """<p>Specifies the trigger type that started the malware scan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TriggerDetails) -> dict:
    out: dict = {}
    if "guard_duty_finding_id" in value:
        out["guardDutyFindingId"] = value["guard_duty_finding_id"]
    if "description" in value:
        out["description"] = value["description"]
    if "trigger_type" in value:
        import capo_guardduty.types.trigger_type

        out["triggerType"] = capo_guardduty.types.trigger_type.serialize_json(
            value["trigger_type"]
        )
    return out


def deserialize_json(data: dict) -> TriggerDetails:
    out: TriggerDetails = {}  # type: ignore[typeddict-item]
    if "guardDutyFindingId" in data:
        out["guard_duty_finding_id"] = data["guardDutyFindingId"]
    if "description" in data:
        out["description"] = data["description"]
    if "triggerType" in data:
        import capo_guardduty.types.trigger_type

        out["trigger_type"] = capo_guardduty.types.trigger_type.deserialize_json(
            data["triggerType"]
        )
    return out

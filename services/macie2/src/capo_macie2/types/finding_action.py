"""Generated from Smithy shape ``com.amazonaws.macie2#FindingAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.api_call_details
    import capo_macie2.types.finding_action_type


class FindingAction(TypedDict, closed=True):
    action_type: NotRequired["capo_macie2.types.finding_action_type.FindingActionType"]
    """<p>The type of action that occurred for the affected resource. This value is typically AWS_API_CALL, which indicates that an entity invoked an API operation for the resource.</p>"""
    api_call_details: NotRequired["capo_macie2.types.api_call_details.ApiCallDetails"]
    """<p>The invocation details of the API operation that an entity invoked for the affected resource, if the value for the actionType property is AWS_API_CALL.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FindingAction) -> dict:
    out: dict = {}
    if "action_type" in value:
        import capo_macie2.types.finding_action_type

        out["actionType"] = capo_macie2.types.finding_action_type.serialize_json(
            value["action_type"]
        )
    if "api_call_details" in value:
        import capo_macie2.types.api_call_details

        out["apiCallDetails"] = capo_macie2.types.api_call_details.serialize_json(
            value["api_call_details"]
        )
    return out


def deserialize_json(data: dict) -> FindingAction:
    out: FindingAction = {}  # type: ignore[typeddict-item]
    if "actionType" in data:
        import capo_macie2.types.finding_action_type

        out["action_type"] = capo_macie2.types.finding_action_type.deserialize_json(
            data["actionType"]
        )
    if "apiCallDetails" in data:
        import capo_macie2.types.api_call_details

        out["api_call_details"] = capo_macie2.types.api_call_details.deserialize_json(
            data["apiCallDetails"]
        )
    return out

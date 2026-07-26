"""Generated from Smithy shape ``com.amazonaws.iot#ListActiveViolationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.behavior_criteria_type
    import capo_iot.types.device_defender_thing_name
    import capo_iot.types.list_suppressed_alerts
    import capo_iot.types.max_results
    import capo_iot.types.next_token
    import capo_iot.types.security_profile_name
    import capo_iot.types.verification_state


class ListActiveViolationsRequest(TypedDict, closed=True):
    thing_name: NotRequired[
        "capo_iot.types.device_defender_thing_name.DeviceDefenderThingName"
    ]
    """<p>The name of the thing whose active violations are listed.</p>"""
    security_profile_name: NotRequired[
        "capo_iot.types.security_profile_name.SecurityProfileName"
    ]
    """<p>The name of the Device Defender security profile for which violations are listed.</p>"""
    behavior_criteria_type: NotRequired[
        "capo_iot.types.behavior_criteria_type.BehaviorCriteriaType"
    ]
    """<p> The criteria for a behavior. </p>"""
    list_suppressed_alerts: NotRequired[
        "capo_iot.types.list_suppressed_alerts.ListSuppressedAlerts"
    ]
    """<p> A list of all suppressed alerts. </p>"""
    verification_state: NotRequired[
        "capo_iot.types.verification_state.VerificationState"
    ]
    """<p>The verification state of the violation (detect alarm).</p>"""
    next_token: NotRequired["capo_iot.types.next_token.NextToken"]
    """<p>The token for the next set of results.</p>"""
    max_results: NotRequired["capo_iot.types.max_results.MaxResults"]
    """<p>The maximum number of results to return at one time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListActiveViolationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListActiveViolationsRequest:
    out: ListActiveViolationsRequest = {}  # type: ignore[typeddict-item]
    return out

"""Generated from Smithy shape ``com.amazonaws.iot#DetectMitigationActionsTaskTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.behavior_name
    import capo_iot.types.security_profile_name
    import capo_iot.types.target_violation_ids_for_detect_mitigation_actions


class DetectMitigationActionsTaskTarget(TypedDict, closed=True):
    violation_ids: NotRequired[
        "capo_iot.types.target_violation_ids_for_detect_mitigation_actions.TargetViolationIdsForDetectMitigationActions"
    ]
    """<p> The unique identifiers of the violations. </p>"""
    security_profile_name: NotRequired[
        "capo_iot.types.security_profile_name.SecurityProfileName"
    ]
    """<p> The name of the security profile. </p>"""
    behavior_name: NotRequired["capo_iot.types.behavior_name.BehaviorName"]
    """<p> The name of the behavior. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DetectMitigationActionsTaskTarget) -> dict:
    out: dict = {}
    if "violation_ids" in value:
        import capo_iot.types.target_violation_ids_for_detect_mitigation_actions

        out["violationIds"] = (
            capo_iot.types.target_violation_ids_for_detect_mitigation_actions.serialize_json(
                value["violation_ids"]
            )
        )
    if "security_profile_name" in value:
        out["securityProfileName"] = value["security_profile_name"]
    if "behavior_name" in value:
        out["behaviorName"] = value["behavior_name"]
    return out


def deserialize_json(data: dict) -> DetectMitigationActionsTaskTarget:
    out: DetectMitigationActionsTaskTarget = {}  # type: ignore[typeddict-item]
    if "violationIds" in data:
        import capo_iot.types.target_violation_ids_for_detect_mitigation_actions

        out["violation_ids"] = (
            capo_iot.types.target_violation_ids_for_detect_mitigation_actions.deserialize_json(
                data["violationIds"]
            )
        )
    if "securityProfileName" in data:
        out["security_profile_name"] = data["securityProfileName"]
    if "behaviorName" in data:
        out["behavior_name"] = data["behaviorName"]
    return out

"""Generated from Smithy shape ``com.amazonaws.iot#ViolationEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.behavior
    import capo_iot.types.device_defender_thing_name
    import capo_iot.types.metric_value
    import capo_iot.types.security_profile_name
    import capo_iot.types.timestamp
    import capo_iot.types.verification_state
    import capo_iot.types.verification_state_description
    import capo_iot.types.violation_event_additional_info
    import capo_iot.types.violation_event_type
    import capo_iot.types.violation_id


class ViolationEvent(TypedDict, closed=True):
    violation_id: NotRequired["capo_iot.types.violation_id.ViolationId"]
    """<p>The ID of the violation event.</p>"""
    thing_name: NotRequired[
        "capo_iot.types.device_defender_thing_name.DeviceDefenderThingName"
    ]
    """<p>The name of the thing responsible for the violation event.</p>"""
    security_profile_name: NotRequired[
        "capo_iot.types.security_profile_name.SecurityProfileName"
    ]
    """<p>The name of the security profile whose behavior was violated.</p>"""
    behavior: NotRequired["capo_iot.types.behavior.Behavior"]
    """<p>The behavior that was violated.</p>"""
    metric_value: NotRequired["capo_iot.types.metric_value.MetricValue"]
    """<p>The value of the metric (the measurement).</p>"""
    violation_event_additional_info: NotRequired[
        "capo_iot.types.violation_event_additional_info.ViolationEventAdditionalInfo"
    ]
    """<p> The details of a violation event. </p>"""
    violation_event_type: NotRequired[
        "capo_iot.types.violation_event_type.ViolationEventType"
    ]
    """<p>The type of violation event.</p>"""
    verification_state: NotRequired[
        "capo_iot.types.verification_state.VerificationState"
    ]
    """<p>The verification state of the violation (detect alarm).</p>"""
    verification_state_description: NotRequired[
        "capo_iot.types.verification_state_description.VerificationStateDescription"
    ]
    """<p>The description of the verification state of the violation.</p>"""
    violation_event_time: NotRequired["capo_iot.types.timestamp.Timestamp"]
    """<p>The time the violation event occurred.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ViolationEvent) -> dict:
    out: dict = {}
    if "violation_id" in value:
        out["violationId"] = value["violation_id"]
    if "thing_name" in value:
        out["thingName"] = value["thing_name"]
    if "security_profile_name" in value:
        out["securityProfileName"] = value["security_profile_name"]
    if "behavior" in value:
        import capo_iot.types.behavior

        out["behavior"] = capo_iot.types.behavior.serialize_json(value["behavior"])
    if "metric_value" in value:
        import capo_iot.types.metric_value

        out["metricValue"] = capo_iot.types.metric_value.serialize_json(
            value["metric_value"]
        )
    if "violation_event_additional_info" in value:
        import capo_iot.types.violation_event_additional_info

        out["violationEventAdditionalInfo"] = (
            capo_iot.types.violation_event_additional_info.serialize_json(
                value["violation_event_additional_info"]
            )
        )
    if "violation_event_type" in value:
        import capo_iot.types.violation_event_type

        out["violationEventType"] = capo_iot.types.violation_event_type.serialize_json(
            value["violation_event_type"]
        )
    if "verification_state" in value:
        import capo_iot.types.verification_state

        out["verificationState"] = capo_iot.types.verification_state.serialize_json(
            value["verification_state"]
        )
    if "verification_state_description" in value:
        out["verificationStateDescription"] = value["verification_state_description"]
    if "violation_event_time" in value:
        import capo_iot.types.timestamp

        out["violationEventTime"] = capo_iot.types.timestamp.serialize_json(
            value["violation_event_time"]
        )
    return out


def deserialize_json(data: dict) -> ViolationEvent:
    out: ViolationEvent = {}  # type: ignore[typeddict-item]
    if "violationId" in data:
        out["violation_id"] = data["violationId"]
    if "thingName" in data:
        out["thing_name"] = data["thingName"]
    if "securityProfileName" in data:
        out["security_profile_name"] = data["securityProfileName"]
    if "behavior" in data:
        import capo_iot.types.behavior

        out["behavior"] = capo_iot.types.behavior.deserialize_json(data["behavior"])
    if "metricValue" in data:
        import capo_iot.types.metric_value

        out["metric_value"] = capo_iot.types.metric_value.deserialize_json(
            data["metricValue"]
        )
    if "violationEventAdditionalInfo" in data:
        import capo_iot.types.violation_event_additional_info

        out["violation_event_additional_info"] = (
            capo_iot.types.violation_event_additional_info.deserialize_json(
                data["violationEventAdditionalInfo"]
            )
        )
    if "violationEventType" in data:
        import capo_iot.types.violation_event_type

        out["violation_event_type"] = (
            capo_iot.types.violation_event_type.deserialize_json(
                data["violationEventType"]
            )
        )
    if "verificationState" in data:
        import capo_iot.types.verification_state

        out["verification_state"] = capo_iot.types.verification_state.deserialize_json(
            data["verificationState"]
        )
    if "verificationStateDescription" in data:
        out["verification_state_description"] = data["verificationStateDescription"]
    if "violationEventTime" in data:
        import capo_iot.types.timestamp

        out["violation_event_time"] = capo_iot.types.timestamp.deserialize_json(
            data["violationEventTime"]
        )
    return out

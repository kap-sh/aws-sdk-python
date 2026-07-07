"""Generated from Smithy shape ``com.amazonaws.iot#ActiveViolation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.behavior
    import aws_sdk_iot.types.device_defender_thing_name
    import aws_sdk_iot.types.metric_value
    import aws_sdk_iot.types.security_profile_name
    import aws_sdk_iot.types.timestamp
    import aws_sdk_iot.types.verification_state
    import aws_sdk_iot.types.verification_state_description
    import aws_sdk_iot.types.violation_event_additional_info
    import aws_sdk_iot.types.violation_id


class ActiveViolation(TypedDict, closed=True):
    violation_id: NotRequired["aws_sdk_iot.types.violation_id.ViolationId"]
    """<p>The ID of the active violation.</p>"""
    thing_name: NotRequired[
        "aws_sdk_iot.types.device_defender_thing_name.DeviceDefenderThingName"
    ]
    """<p>The name of the thing responsible for the active violation.</p>"""
    security_profile_name: NotRequired[
        "aws_sdk_iot.types.security_profile_name.SecurityProfileName"
    ]
    """<p>The security profile with the behavior is in violation.</p>"""
    behavior: NotRequired["aws_sdk_iot.types.behavior.Behavior"]
    """<p>The behavior that is being violated.</p>"""
    last_violation_value: NotRequired["aws_sdk_iot.types.metric_value.MetricValue"]
    """<p>The value of the metric (the measurement) that caused the most recent violation.</p>"""
    violation_event_additional_info: NotRequired[
        "aws_sdk_iot.types.violation_event_additional_info.ViolationEventAdditionalInfo"
    ]
    """<p> The details of a violation event. </p>"""
    verification_state: NotRequired[
        "aws_sdk_iot.types.verification_state.VerificationState"
    ]
    """<p>The verification state of the violation (detect alarm).</p>"""
    verification_state_description: NotRequired[
        "aws_sdk_iot.types.verification_state_description.VerificationStateDescription"
    ]
    """<p>The description of the verification state of the violation.</p>"""
    last_violation_time: NotRequired["aws_sdk_iot.types.timestamp.Timestamp"]
    """<p>The time the most recent violation occurred.</p>"""
    violation_start_time: NotRequired["aws_sdk_iot.types.timestamp.Timestamp"]
    """<p>The time the violation started.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActiveViolation) -> dict:
    out: dict = {}
    if "violation_id" in value:
        out["violationId"] = value["violation_id"]
    if "thing_name" in value:
        out["thingName"] = value["thing_name"]
    if "security_profile_name" in value:
        out["securityProfileName"] = value["security_profile_name"]
    if "behavior" in value:
        import aws_sdk_iot.types.behavior

        out["behavior"] = aws_sdk_iot.types.behavior.serialize_json(value["behavior"])
    if "last_violation_value" in value:
        import aws_sdk_iot.types.metric_value

        out["lastViolationValue"] = aws_sdk_iot.types.metric_value.serialize_json(
            value["last_violation_value"]
        )
    if "violation_event_additional_info" in value:
        import aws_sdk_iot.types.violation_event_additional_info

        out["violationEventAdditionalInfo"] = (
            aws_sdk_iot.types.violation_event_additional_info.serialize_json(
                value["violation_event_additional_info"]
            )
        )
    if "verification_state" in value:
        import aws_sdk_iot.types.verification_state

        out["verificationState"] = aws_sdk_iot.types.verification_state.serialize_json(
            value["verification_state"]
        )
    if "verification_state_description" in value:
        out["verificationStateDescription"] = value["verification_state_description"]
    if "last_violation_time" in value:
        import aws_sdk_iot.types.timestamp

        out["lastViolationTime"] = aws_sdk_iot.types.timestamp.serialize_json(
            value["last_violation_time"]
        )
    if "violation_start_time" in value:
        import aws_sdk_iot.types.timestamp

        out["violationStartTime"] = aws_sdk_iot.types.timestamp.serialize_json(
            value["violation_start_time"]
        )
    return out


def deserialize_json(data: dict) -> ActiveViolation:
    out: ActiveViolation = {}  # type: ignore[typeddict-item]
    if "violationId" in data:
        out["violation_id"] = data["violationId"]
    if "thingName" in data:
        out["thing_name"] = data["thingName"]
    if "securityProfileName" in data:
        out["security_profile_name"] = data["securityProfileName"]
    if "behavior" in data:
        import aws_sdk_iot.types.behavior

        out["behavior"] = aws_sdk_iot.types.behavior.deserialize_json(data["behavior"])
    if "lastViolationValue" in data:
        import aws_sdk_iot.types.metric_value

        out["last_violation_value"] = aws_sdk_iot.types.metric_value.deserialize_json(
            data["lastViolationValue"]
        )
    if "violationEventAdditionalInfo" in data:
        import aws_sdk_iot.types.violation_event_additional_info

        out["violation_event_additional_info"] = (
            aws_sdk_iot.types.violation_event_additional_info.deserialize_json(
                data["violationEventAdditionalInfo"]
            )
        )
    if "verificationState" in data:
        import aws_sdk_iot.types.verification_state

        out["verification_state"] = (
            aws_sdk_iot.types.verification_state.deserialize_json(
                data["verificationState"]
            )
        )
    if "verificationStateDescription" in data:
        out["verification_state_description"] = data["verificationStateDescription"]
    if "lastViolationTime" in data:
        import aws_sdk_iot.types.timestamp

        out["last_violation_time"] = aws_sdk_iot.types.timestamp.deserialize_json(
            data["lastViolationTime"]
        )
    if "violationStartTime" in data:
        import aws_sdk_iot.types.timestamp

        out["violation_start_time"] = aws_sdk_iot.types.timestamp.deserialize_json(
            data["violationStartTime"]
        )
    return out

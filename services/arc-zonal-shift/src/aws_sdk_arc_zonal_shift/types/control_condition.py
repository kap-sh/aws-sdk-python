"""Generated from Smithy shape ``com.amazonaws.arczonalshift#ControlCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_arc_zonal_shift.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_arc_zonal_shift.types.control_condition_type
    import aws_sdk_arc_zonal_shift.types.metric_identifier


class ControlCondition(TypedDict, closed=True):
    type: "aws_sdk_arc_zonal_shift.types.control_condition_type.ControlConditionType"
    """<p>The type of alarm specified for a practice run. You can only specify Amazon CloudWatch alarms for practice runs, so the only valid value is <code>CLOUDWATCH</code>.</p>"""
    alarm_identifier: "aws_sdk_arc_zonal_shift.types.metric_identifier.MetricIdentifier"
    """<p>The Amazon Resource Name (ARN) for an Amazon CloudWatch alarm that you specify as a control condition for a practice run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ControlCondition) -> dict:
    out: dict = {}
    import aws_sdk_arc_zonal_shift.types.control_condition_type

    out["type"] = aws_sdk_arc_zonal_shift.types.control_condition_type.serialize_json(
        value["type"]
    )
    out["alarmIdentifier"] = value["alarm_identifier"]
    return out


def deserialize_json(data: dict) -> ControlCondition:
    out: ControlCondition = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_arc_zonal_shift.types.control_condition_type

        out["type"] = (
            aws_sdk_arc_zonal_shift.types.control_condition_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError("ControlCondition.type required")
    if "alarmIdentifier" in data:
        out["alarm_identifier"] = data["alarmIdentifier"]
    else:
        raise DeserializationError("ControlCondition.alarm_identifier required")
    return out

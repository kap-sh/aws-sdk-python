"""Generated from Smithy shape ``com.amazonaws.iot#CloudwatchAlarmAction``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.alarm_name
    import aws_sdk_iot.types.aws_arn
    import aws_sdk_iot.types.state_reason
    import aws_sdk_iot.types.state_value


class CloudwatchAlarmAction(TypedDict, closed=True):
    role_arn: "aws_sdk_iot.types.aws_arn.AwsArn"
    """<p>The IAM role that allows access to the CloudWatch alarm.</p>"""
    alarm_name: "aws_sdk_iot.types.alarm_name.AlarmName"
    """<p>The CloudWatch alarm name.</p>"""
    state_reason: "aws_sdk_iot.types.state_reason.StateReason"
    """<p>The reason for the alarm change.</p>"""
    state_value: "aws_sdk_iot.types.state_value.StateValue"
    """<p>The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudwatchAlarmAction) -> dict:
    out: dict = {}
    out["roleArn"] = value["role_arn"]
    out["alarmName"] = value["alarm_name"]
    out["stateReason"] = value["state_reason"]
    out["stateValue"] = value["state_value"]
    return out


def deserialize_json(data: dict) -> CloudwatchAlarmAction:
    out: CloudwatchAlarmAction = {}  # type: ignore[typeddict-item]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("CloudwatchAlarmAction.role_arn required")
    if "alarmName" in data:
        out["alarm_name"] = data["alarmName"]
    else:
        raise DeserializationError("CloudwatchAlarmAction.alarm_name required")
    if "stateReason" in data:
        out["state_reason"] = data["stateReason"]
    else:
        raise DeserializationError("CloudwatchAlarmAction.state_reason required")
    if "stateValue" in data:
        out["state_value"] = data["stateValue"]
    else:
        raise DeserializationError("CloudwatchAlarmAction.state_value required")
    return out

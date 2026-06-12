"""Generated from Smithy shape ``com.amazonaws.ssm#AlarmConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.alarm_list
    import aws_sdk_ssm.types.boolean


class AlarmConfiguration(TypedDict):
    ignore_poll_alarm_failure: "aws_sdk_ssm.types.boolean.Boolean"
    """<p>When this value is <i>true</i>, your automation or command continues to run in cases where we can’t retrieve alarm status information from CloudWatch. In cases where we successfully retrieve an alarm status of OK or INSUFFICIENT_DATA, the automation or command continues to run, regardless of this value. Default is <i>false</i>.</p>"""
    alarms: "aws_sdk_ssm.types.alarm_list.AlarmList"
    """<p>The name of the CloudWatch alarm specified in the configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AlarmConfiguration) -> dict:
    out: dict = {}
    out["IgnorePollAlarmFailure"] = value.get("ignore_poll_alarm_failure", False)
    import aws_sdk_ssm.types.alarm_list

    out["Alarms"] = aws_sdk_ssm.types.alarm_list.serialize_aws_json_1_1(value["alarms"])
    return out


def deserialize_aws_json_1_1(data: dict) -> AlarmConfiguration:
    out: AlarmConfiguration = {}  # type: ignore[typeddict-item]
    if "IgnorePollAlarmFailure" in data:
        out["ignore_poll_alarm_failure"] = data["IgnorePollAlarmFailure"]
    else:
        out["ignore_poll_alarm_failure"] = False
    if "Alarms" in data:
        import aws_sdk_ssm.types.alarm_list

        out["alarms"] = aws_sdk_ssm.types.alarm_list.deserialize_aws_json_1_1(
            data["Alarms"]
        )
    else:
        raise DeserializationError("AlarmConfiguration.alarms required")
    return out

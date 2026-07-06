"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#Alarm``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_application_auto_scaling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_auto_scaling.types.resource_id


class Alarm(TypedDict, closed=True):
    alarm_name: "aws_sdk_application_auto_scaling.types.resource_id.ResourceId"
    """<p>The name of the alarm.</p>"""
    alarm_arn: "aws_sdk_application_auto_scaling.types.resource_id.ResourceId"
    """<p>The Amazon Resource Name (ARN) of the alarm.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Alarm) -> dict:
    out: dict = {}
    out["AlarmName"] = value["alarm_name"]
    out["AlarmARN"] = value["alarm_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Alarm:
    out: Alarm = {}  # type: ignore[typeddict-item]
    if "AlarmName" in data:
        out["alarm_name"] = data["AlarmName"]
    else:
        raise DeserializationError("Alarm.alarm_name required")
    if "AlarmARN" in data:
        out["alarm_arn"] = data["AlarmARN"]
    else:
        raise DeserializationError("Alarm.alarm_arn required")
    return out

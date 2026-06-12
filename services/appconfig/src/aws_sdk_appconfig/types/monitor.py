"""Generated from Smithy shape ``com.amazonaws.appconfig#Monitor``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_appconfig.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.role_arn
    import aws_sdk_appconfig.types.string_with_length_between1_and2048


class Monitor(TypedDict):
    alarm_arn: "aws_sdk_appconfig.types.string_with_length_between1_and2048.StringWithLengthBetween1And2048"
    """<p>Amazon Resource Name (ARN) of the Amazon CloudWatch alarm.</p>"""
    alarm_role_arn: NotRequired["aws_sdk_appconfig.types.role_arn.RoleArn"]
    """<p>ARN of an Identity and Access Management (IAM) role for AppConfig to monitor <code>AlarmArn</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Monitor) -> dict:
    out: dict = {}
    out["AlarmArn"] = value["alarm_arn"]
    if "alarm_role_arn" in value:
        out["AlarmRoleArn"] = value["alarm_role_arn"]
    return out


def deserialize_json(data: dict) -> Monitor:
    out: Monitor = {}  # type: ignore[typeddict-item]
    if "AlarmArn" in data:
        out["alarm_arn"] = data["AlarmArn"]
    else:
        raise DeserializationError("Monitor.alarm_arn required")
    if "AlarmRoleArn" in data:
        out["alarm_role_arn"] = data["AlarmRoleArn"]
    return out

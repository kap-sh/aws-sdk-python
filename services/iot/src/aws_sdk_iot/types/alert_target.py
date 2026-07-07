"""Generated from Smithy shape ``com.amazonaws.iot#AlertTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.alert_target_arn
    import aws_sdk_iot.types.role_arn


class AlertTarget(TypedDict, closed=True):
    alert_target_arn: "aws_sdk_iot.types.alert_target_arn.AlertTargetArn"
    """<p>The Amazon Resource Name (ARN) of the notification target to which alerts are sent.</p>"""
    role_arn: "aws_sdk_iot.types.role_arn.RoleArn"
    """<p>The ARN of the role that grants permission to send alerts to the notification target.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AlertTarget) -> dict:
    out: dict = {}
    out["alertTargetArn"] = value["alert_target_arn"]
    out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> AlertTarget:
    out: AlertTarget = {}  # type: ignore[typeddict-item]
    if "alertTargetArn" in data:
        out["alert_target_arn"] = data["alertTargetArn"]
    else:
        raise DeserializationError("AlertTarget.alert_target_arn required")
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("AlertTarget.role_arn required")
    return out

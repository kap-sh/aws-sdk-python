"""Generated from Smithy shape ``com.amazonaws.iot#AuditNotificationTarget``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.enabled
    import aws_sdk_iot.types.role_arn
    import aws_sdk_iot.types.target_arn


class AuditNotificationTarget(TypedDict):
    target_arn: NotRequired["aws_sdk_iot.types.target_arn.TargetArn"]
    """<p>The ARN of the target (SNS topic) to which audit notifications are sent.</p>"""
    role_arn: NotRequired["aws_sdk_iot.types.role_arn.RoleArn"]
    """<p>The ARN of the role that grants permission to send notifications to the target.</p>"""
    enabled: "aws_sdk_iot.types.enabled.Enabled"
    """<p>True if notifications to the target are enabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuditNotificationTarget) -> dict:
    out: dict = {}
    if "target_arn" in value:
        out["targetArn"] = value["target_arn"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    out["enabled"] = value.get("enabled", False)
    return out


def deserialize_json(data: dict) -> AuditNotificationTarget:
    out: AuditNotificationTarget = {}  # type: ignore[typeddict-item]
    if "targetArn" in data:
        out["target_arn"] = data["targetArn"]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    else:
        out["enabled"] = False
    return out

"""Generated from Smithy shape ``com.amazonaws.iot#UpdateAccountAuditConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.audit_check_configurations
    import aws_sdk_iot.types.audit_notification_target_configurations
    import aws_sdk_iot.types.role_arn


class UpdateAccountAuditConfigurationRequest(TypedDict):
    role_arn: NotRequired["aws_sdk_iot.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the role that grants permission to IoT to access information about your devices, policies, certificates, and other items as required when performing an audit.</p>"""
    audit_notification_target_configurations: NotRequired[
        "aws_sdk_iot.types.audit_notification_target_configurations.AuditNotificationTargetConfigurations"
    ]
    """<p>Information about the targets to which audit notifications are sent.</p>"""
    audit_check_configurations: NotRequired[
        "aws_sdk_iot.types.audit_check_configurations.AuditCheckConfigurations"
    ]
    """<p>Specifies which audit checks are enabled and disabled for this account. Use <code>DescribeAccountAuditConfiguration</code> to see the list of all checks, including those that are currently enabled.</p> <p>Some data collection might start immediately when certain checks are enabled. When a check is disabled, any data collected so far in relation to the check is deleted.</p> <p>You cannot disable a check if it's used by any scheduled audit. You must first delete the check from the scheduled audit or delete the scheduled audit itself.</p> <p>On the first call to <code>UpdateAccountAuditConfiguration</code>, this parameter is required and must specify at least one enabled check.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAccountAuditConfigurationRequest) -> dict:
    out: dict = {}
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "audit_notification_target_configurations" in value:
        import aws_sdk_iot.types.audit_notification_target_configurations

        out["auditNotificationTargetConfigurations"] = (
            aws_sdk_iot.types.audit_notification_target_configurations.serialize_json(
                value["audit_notification_target_configurations"]
            )
        )
    if "audit_check_configurations" in value:
        import aws_sdk_iot.types.audit_check_configurations

        out["auditCheckConfigurations"] = (
            aws_sdk_iot.types.audit_check_configurations.serialize_json(
                value["audit_check_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateAccountAuditConfigurationRequest:
    out: UpdateAccountAuditConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "auditNotificationTargetConfigurations" in data:
        import aws_sdk_iot.types.audit_notification_target_configurations

        out["audit_notification_target_configurations"] = (
            aws_sdk_iot.types.audit_notification_target_configurations.deserialize_json(
                data["auditNotificationTargetConfigurations"]
            )
        )
    if "auditCheckConfigurations" in data:
        import aws_sdk_iot.types.audit_check_configurations

        out["audit_check_configurations"] = (
            aws_sdk_iot.types.audit_check_configurations.deserialize_json(
                data["auditCheckConfigurations"]
            )
        )
    return out

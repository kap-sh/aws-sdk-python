"""Generated from Smithy shape ``com.amazonaws.iot#AuditNotificationTargetConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.audit_notification_target
    import aws_sdk_iot.types.audit_notification_type

AuditNotificationTargetConfigurations: TypeAlias = dict[
    "aws_sdk_iot.types.audit_notification_type.AuditNotificationType",
    "aws_sdk_iot.types.audit_notification_target.AuditNotificationTarget",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: AuditNotificationTargetConfigurations) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_iot.types.audit_notification_target
        import aws_sdk_iot.types.audit_notification_type

        out[aws_sdk_iot.types.audit_notification_type.serialize_json(key)] = (
            aws_sdk_iot.types.audit_notification_target.serialize_json(value)
        )
    return out


def deserialize_json(data: dict) -> AuditNotificationTargetConfigurations:
    out: AuditNotificationTargetConfigurations = {}
    for key, value in data.items():
        import aws_sdk_iot.types.audit_notification_target
        import aws_sdk_iot.types.audit_notification_type

        out[aws_sdk_iot.types.audit_notification_type.deserialize_json(key)] = (
            aws_sdk_iot.types.audit_notification_target.deserialize_json(value)
        )
    return out

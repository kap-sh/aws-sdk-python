"""Generated from Smithy shape ``com.amazonaws.iot#AuditNotificationTargetConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.audit_notification_target
    import capo_iot.types.audit_notification_type

AuditNotificationTargetConfigurations: TypeAlias = dict[
    "capo_iot.types.audit_notification_type.AuditNotificationType",
    "capo_iot.types.audit_notification_target.AuditNotificationTarget",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: AuditNotificationTargetConfigurations) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_iot.types.audit_notification_target
        import capo_iot.types.audit_notification_type

        out[capo_iot.types.audit_notification_type.serialize_json(key)] = (
            capo_iot.types.audit_notification_target.serialize_json(value)
        )
    return out


def deserialize_json(data: dict) -> AuditNotificationTargetConfigurations:
    out: AuditNotificationTargetConfigurations = {}
    for key, value in data.items():
        import capo_iot.types.audit_notification_target
        import capo_iot.types.audit_notification_type

        out[capo_iot.types.audit_notification_type.deserialize_json(key)] = (
            capo_iot.types.audit_notification_target.deserialize_json(value)
        )
    return out

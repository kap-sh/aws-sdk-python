"""Generated from Smithy shape ``com.amazonaws.auditmanager#Notifications``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.notification

Notifications: TypeAlias = list["aws_sdk_auditmanager.types.notification.Notification"]


# --- restJson1 ser/de ---
def serialize_json(value: Notifications) -> list:
    import aws_sdk_auditmanager.types.notification

    out: list = []
    for item in value:
        out.append(aws_sdk_auditmanager.types.notification.serialize_json(item))
    return out


def deserialize_json(data: list) -> Notifications:
    import aws_sdk_auditmanager.types.notification

    out: Notifications = []
    for item in data:
        out.append(aws_sdk_auditmanager.types.notification.deserialize_json(item))
    return out

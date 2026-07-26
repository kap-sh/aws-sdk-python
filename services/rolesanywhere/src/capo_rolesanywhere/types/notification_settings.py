"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#NotificationSettings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rolesanywhere.types.notification_setting

NotificationSettings: TypeAlias = list[
    "capo_rolesanywhere.types.notification_setting.NotificationSetting"
]


# --- restJson1 ser/de ---
def serialize_json(value: NotificationSettings) -> list:
    import capo_rolesanywhere.types.notification_setting

    out: list = []
    for item in value:
        out.append(capo_rolesanywhere.types.notification_setting.serialize_json(item))
    return out


def deserialize_json(data: list) -> NotificationSettings:
    import capo_rolesanywhere.types.notification_setting

    out: NotificationSettings = []
    for item in data:
        out.append(capo_rolesanywhere.types.notification_setting.deserialize_json(item))
    return out

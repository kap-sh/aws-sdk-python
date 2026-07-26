"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#NotificationSettingKeys``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rolesanywhere.types.notification_setting_key

NotificationSettingKeys: TypeAlias = list[
    "capo_rolesanywhere.types.notification_setting_key.NotificationSettingKey"
]


# --- restJson1 ser/de ---
def serialize_json(value: NotificationSettingKeys) -> list:
    import capo_rolesanywhere.types.notification_setting_key

    out: list = []
    for item in value:
        out.append(
            capo_rolesanywhere.types.notification_setting_key.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> NotificationSettingKeys:
    import capo_rolesanywhere.types.notification_setting_key

    out: NotificationSettingKeys = []
    for item in data:
        out.append(
            capo_rolesanywhere.types.notification_setting_key.deserialize_json(item)
        )
    return out

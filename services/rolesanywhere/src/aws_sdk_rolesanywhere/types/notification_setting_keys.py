"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#NotificationSettingKeys``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rolesanywhere.types.notification_setting_key

NotificationSettingKeys: TypeAlias = list[
    "aws_sdk_rolesanywhere.types.notification_setting_key.NotificationSettingKey"
]


# --- restJson1 ser/de ---
def serialize_json(value: NotificationSettingKeys) -> list:
    import aws_sdk_rolesanywhere.types.notification_setting_key

    out: list = []
    for item in value:
        out.append(
            aws_sdk_rolesanywhere.types.notification_setting_key.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> NotificationSettingKeys:
    import aws_sdk_rolesanywhere.types.notification_setting_key

    out: NotificationSettingKeys = []
    for item in data:
        out.append(
            aws_sdk_rolesanywhere.types.notification_setting_key.deserialize_json(item)
        )
    return out

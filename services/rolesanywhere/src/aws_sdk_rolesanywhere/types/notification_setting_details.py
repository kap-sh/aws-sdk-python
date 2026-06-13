"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#NotificationSettingDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rolesanywhere.types.notification_setting_detail

NotificationSettingDetails: TypeAlias = list[
    "aws_sdk_rolesanywhere.types.notification_setting_detail.NotificationSettingDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: NotificationSettingDetails) -> list:
    import aws_sdk_rolesanywhere.types.notification_setting_detail

    out: list = []
    for item in value:
        out.append(
            aws_sdk_rolesanywhere.types.notification_setting_detail.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> NotificationSettingDetails:
    import aws_sdk_rolesanywhere.types.notification_setting_detail

    out: NotificationSettingDetails = []
    for item in data:
        out.append(
            aws_sdk_rolesanywhere.types.notification_setting_detail.deserialize_json(
                item
            )
        )
    return out

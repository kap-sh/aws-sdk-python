"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#ResetNotificationSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_rolesanywhere.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rolesanywhere.types.notification_setting_keys
    import capo_rolesanywhere.types.uuid


class ResetNotificationSettingsRequest(TypedDict, closed=True):
    trust_anchor_id: "capo_rolesanywhere.types.uuid.Uuid"
    """<p>The unique identifier of the trust anchor.</p>"""
    notification_setting_keys: (
        "capo_rolesanywhere.types.notification_setting_keys.NotificationSettingKeys"
    )
    """<p>A list of notification setting keys to reset. A notification setting key includes the event and the channel. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResetNotificationSettingsRequest) -> dict:
    out: dict = {}
    out["trustAnchorId"] = value["trust_anchor_id"]
    import capo_rolesanywhere.types.notification_setting_keys

    out["notificationSettingKeys"] = (
        capo_rolesanywhere.types.notification_setting_keys.serialize_json(
            value["notification_setting_keys"]
        )
    )
    return out


def deserialize_json(data: dict) -> ResetNotificationSettingsRequest:
    out: ResetNotificationSettingsRequest = {}  # type: ignore[typeddict-item]
    if "trustAnchorId" in data:
        out["trust_anchor_id"] = data["trustAnchorId"]
    else:
        raise DeserializationError(
            "ResetNotificationSettingsRequest.trust_anchor_id required"
        )
    if "notificationSettingKeys" in data:
        import capo_rolesanywhere.types.notification_setting_keys

        out["notification_setting_keys"] = (
            capo_rolesanywhere.types.notification_setting_keys.deserialize_json(
                data["notificationSettingKeys"]
            )
        )
    else:
        raise DeserializationError(
            "ResetNotificationSettingsRequest.notification_setting_keys required"
        )
    return out

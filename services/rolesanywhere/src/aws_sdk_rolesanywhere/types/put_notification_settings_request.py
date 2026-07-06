"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#PutNotificationSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_rolesanywhere.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rolesanywhere.types.notification_settings
    import aws_sdk_rolesanywhere.types.uuid


class PutNotificationSettingsRequest(TypedDict, closed=True):
    trust_anchor_id: "aws_sdk_rolesanywhere.types.uuid.Uuid"
    """<p>The unique identifier of the trust anchor.</p>"""
    notification_settings: (
        "aws_sdk_rolesanywhere.types.notification_settings.NotificationSettings"
    )
    """<p>A list of notification settings to be associated to the trust anchor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutNotificationSettingsRequest) -> dict:
    out: dict = {}
    out["trustAnchorId"] = value["trust_anchor_id"]
    import aws_sdk_rolesanywhere.types.notification_settings

    out["notificationSettings"] = (
        aws_sdk_rolesanywhere.types.notification_settings.serialize_json(
            value["notification_settings"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutNotificationSettingsRequest:
    out: PutNotificationSettingsRequest = {}  # type: ignore[typeddict-item]
    if "trustAnchorId" in data:
        out["trust_anchor_id"] = data["trustAnchorId"]
    else:
        raise DeserializationError(
            "PutNotificationSettingsRequest.trust_anchor_id required"
        )
    if "notificationSettings" in data:
        import aws_sdk_rolesanywhere.types.notification_settings

        out["notification_settings"] = (
            aws_sdk_rolesanywhere.types.notification_settings.deserialize_json(
                data["notificationSettings"]
            )
        )
    else:
        raise DeserializationError(
            "PutNotificationSettingsRequest.notification_settings required"
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.notifications#ManagedNotificationChannelAssociationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import capo_notifications.types.channel_association_override_option
    import capo_notifications.types.channel_type


class ManagedNotificationChannelAssociationSummary(TypedDict, closed=True):
    channel_identifier: "str"
    """<p>The unique identifier for the notification channel.</p>"""
    channel_type: "capo_notifications.types.channel_type.ChannelType"
    """<p>The type of notification channel used for message delivery.</p> <ul> <li> <p>Values:</p> <ul> <li> <p> <code>ACCOUNT_CONTACT</code> </p> <ul> <li> <p>Delivers notifications to Account Managed contacts through the User Notification Service.</p> </li> </ul> </li> <li> <p> <code>MOBILE</code> </p> <ul> <li> <p>Delivers notifications through the Amazon Web Services Console Mobile Application to mobile devices.</p> </li> </ul> </li> <li> <p> <code>CHATBOT</code> </p> <ul> <li> <p>Delivers notifications through Amazon Q Developer in chat applications to collaboration platforms (Slack, Chime).</p> </li> </ul> </li> <li> <p> <code>EMAIL</code> </p> <ul> <li> <p>Delivers notifications to email addresses.</p> </li> </ul> </li> </ul> </li> </ul>"""
    override_option: NotRequired[
        "capo_notifications.types.channel_association_override_option.ChannelAssociationOverrideOption"
    ]
    """<p>Controls whether users can modify channel associations for a notification configuration.</p> <ul> <li> <p>Values:</p> <ul> <li> <p> <code>ENABLED</code> </p> <ul> <li> <p>Users can associate or disassociate channels with the notification configuration.</p> </li> </ul> </li> <li> <p> <code>DISABLED</code> </p> <ul> <li> <p>Users cannot associate or disassociate channels with the notification configuration.</p> </li> </ul> </li> </ul> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManagedNotificationChannelAssociationSummary) -> dict:
    out: dict = {}
    out["channelIdentifier"] = value["channel_identifier"]
    out["channelType"] = value["channel_type"]
    if "override_option" in value:
        out["overrideOption"] = value["override_option"]
    return out


def deserialize_json(data: dict) -> ManagedNotificationChannelAssociationSummary:
    out: ManagedNotificationChannelAssociationSummary = {}  # type: ignore[typeddict-item]
    if "channelIdentifier" in data:
        out["channel_identifier"] = data["channelIdentifier"]
    else:
        raise DeserializationError(
            "ManagedNotificationChannelAssociationSummary.channel_identifier required"
        )
    if "channelType" in data:
        out["channel_type"] = data["channelType"]
    else:
        raise DeserializationError(
            "ManagedNotificationChannelAssociationSummary.channel_type required"
        )
    if "overrideOption" in data:
        out["override_option"] = data["overrideOption"]
    return out

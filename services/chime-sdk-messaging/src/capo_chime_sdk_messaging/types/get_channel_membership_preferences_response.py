"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#GetChannelMembershipPreferencesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.channel_membership_preferences
    import capo_chime_sdk_messaging.types.chime_arn
    import capo_chime_sdk_messaging.types.identity


class GetChannelMembershipPreferencesResponse(TypedDict, closed=True):
    channel_arn: NotRequired["capo_chime_sdk_messaging.types.chime_arn.ChimeArn"]
    """<p>The ARN of the channel.</p>"""
    member: NotRequired["capo_chime_sdk_messaging.types.identity.Identity"]
    """<p>The details of a user.</p>"""
    preferences: NotRequired[
        "capo_chime_sdk_messaging.types.channel_membership_preferences.ChannelMembershipPreferences"
    ]
    """<p>The channel membership preferences for an <code>AppInstanceUser</code> .</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetChannelMembershipPreferencesResponse) -> dict:
    out: dict = {}
    if "channel_arn" in value:
        out["ChannelArn"] = value["channel_arn"]
    if "member" in value:
        import capo_chime_sdk_messaging.types.identity

        out["Member"] = capo_chime_sdk_messaging.types.identity.serialize_json(
            value["member"]
        )
    if "preferences" in value:
        import capo_chime_sdk_messaging.types.channel_membership_preferences

        out["Preferences"] = (
            capo_chime_sdk_messaging.types.channel_membership_preferences.serialize_json(
                value["preferences"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetChannelMembershipPreferencesResponse:
    out: GetChannelMembershipPreferencesResponse = {}  # type: ignore[typeddict-item]
    if "ChannelArn" in data:
        out["channel_arn"] = data["ChannelArn"]
    if "Member" in data:
        import capo_chime_sdk_messaging.types.identity

        out["member"] = capo_chime_sdk_messaging.types.identity.deserialize_json(
            data["Member"]
        )
    if "Preferences" in data:
        import capo_chime_sdk_messaging.types.channel_membership_preferences

        out["preferences"] = (
            capo_chime_sdk_messaging.types.channel_membership_preferences.deserialize_json(
                data["Preferences"]
            )
        )
    return out

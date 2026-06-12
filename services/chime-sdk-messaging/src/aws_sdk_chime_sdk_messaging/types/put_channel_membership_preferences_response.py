"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#PutChannelMembershipPreferencesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.channel_membership_preferences
    import aws_sdk_chime_sdk_messaging.types.chime_arn
    import aws_sdk_chime_sdk_messaging.types.identity


class PutChannelMembershipPreferencesResponse(TypedDict):
    channel_arn: NotRequired["aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"]
    """<p>The ARN of the channel.</p>"""
    member: NotRequired["aws_sdk_chime_sdk_messaging.types.identity.Identity"]
    """<p>The details of a user.</p>"""
    preferences: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.channel_membership_preferences.ChannelMembershipPreferences"
    ]
    """<p>The ARN and metadata of the member being added.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutChannelMembershipPreferencesResponse) -> dict:
    out: dict = {}
    if "channel_arn" in value:
        out["ChannelArn"] = value["channel_arn"]
    if "member" in value:
        import aws_sdk_chime_sdk_messaging.types.identity

        out["Member"] = aws_sdk_chime_sdk_messaging.types.identity.serialize_json(
            value["member"]
        )
    if "preferences" in value:
        import aws_sdk_chime_sdk_messaging.types.channel_membership_preferences

        out["Preferences"] = (
            aws_sdk_chime_sdk_messaging.types.channel_membership_preferences.serialize_json(
                value["preferences"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutChannelMembershipPreferencesResponse:
    out: PutChannelMembershipPreferencesResponse = {}  # type: ignore[typeddict-item]
    if "ChannelArn" in data:
        out["channel_arn"] = data["ChannelArn"]
    if "Member" in data:
        import aws_sdk_chime_sdk_messaging.types.identity

        out["member"] = aws_sdk_chime_sdk_messaging.types.identity.deserialize_json(
            data["Member"]
        )
    if "Preferences" in data:
        import aws_sdk_chime_sdk_messaging.types.channel_membership_preferences

        out["preferences"] = (
            aws_sdk_chime_sdk_messaging.types.channel_membership_preferences.deserialize_json(
                data["Preferences"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#PutChannelMembershipPreferencesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_chime_sdk_messaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.channel_membership_preferences
    import aws_sdk_chime_sdk_messaging.types.chime_arn


class PutChannelMembershipPreferencesRequest(TypedDict):
    channel_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the channel.</p>"""
    member_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the member setting the preferences.</p>"""
    chime_bearer: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>"""
    preferences: "aws_sdk_chime_sdk_messaging.types.channel_membership_preferences.ChannelMembershipPreferences"
    """<p>The channel membership preferences of an <code>AppInstanceUser</code> .</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutChannelMembershipPreferencesRequest) -> dict:
    out: dict = {}
    import aws_sdk_chime_sdk_messaging.types.channel_membership_preferences

    out["Preferences"] = (
        aws_sdk_chime_sdk_messaging.types.channel_membership_preferences.serialize_json(
            value["preferences"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutChannelMembershipPreferencesRequest:
    out: PutChannelMembershipPreferencesRequest = {}  # type: ignore[typeddict-item]
    if "Preferences" in data:
        import aws_sdk_chime_sdk_messaging.types.channel_membership_preferences

        out["preferences"] = (
            aws_sdk_chime_sdk_messaging.types.channel_membership_preferences.deserialize_json(
                data["Preferences"]
            )
        )
    else:
        raise DeserializationError(
            "PutChannelMembershipPreferencesRequest.preferences required"
        )
    return out

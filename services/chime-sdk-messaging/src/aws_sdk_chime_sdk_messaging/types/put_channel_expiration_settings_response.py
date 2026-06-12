"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#PutChannelExpirationSettingsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.chime_arn
    import aws_sdk_chime_sdk_messaging.types.expiration_settings


class PutChannelExpirationSettingsResponse(TypedDict):
    channel_arn: NotRequired["aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"]
    """<p>The channel ARN.</p>"""
    expiration_settings: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.expiration_settings.ExpirationSettings"
    ]
    """<p>Settings that control the interval after which a channel is deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutChannelExpirationSettingsResponse) -> dict:
    out: dict = {}
    if "channel_arn" in value:
        out["ChannelArn"] = value["channel_arn"]
    if "expiration_settings" in value:
        import aws_sdk_chime_sdk_messaging.types.expiration_settings

        out["ExpirationSettings"] = (
            aws_sdk_chime_sdk_messaging.types.expiration_settings.serialize_json(
                value["expiration_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutChannelExpirationSettingsResponse:
    out: PutChannelExpirationSettingsResponse = {}  # type: ignore[typeddict-item]
    if "ChannelArn" in data:
        out["channel_arn"] = data["ChannelArn"]
    if "ExpirationSettings" in data:
        import aws_sdk_chime_sdk_messaging.types.expiration_settings

        out["expiration_settings"] = (
            aws_sdk_chime_sdk_messaging.types.expiration_settings.deserialize_json(
                data["ExpirationSettings"]
            )
        )
    return out

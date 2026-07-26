"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#PutChannelExpirationSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.chime_arn
    import capo_chime_sdk_messaging.types.expiration_settings


class PutChannelExpirationSettingsRequest(TypedDict, closed=True):
    channel_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the channel.</p>"""
    chime_bearer: NotRequired["capo_chime_sdk_messaging.types.chime_arn.ChimeArn"]
    """<p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>"""
    expiration_settings: NotRequired[
        "capo_chime_sdk_messaging.types.expiration_settings.ExpirationSettings"
    ]
    """<p>Settings that control the interval after which a channel is deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutChannelExpirationSettingsRequest) -> dict:
    out: dict = {}
    if "expiration_settings" in value:
        import capo_chime_sdk_messaging.types.expiration_settings

        out["ExpirationSettings"] = (
            capo_chime_sdk_messaging.types.expiration_settings.serialize_json(
                value["expiration_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutChannelExpirationSettingsRequest:
    out: PutChannelExpirationSettingsRequest = {}  # type: ignore[typeddict-item]
    if "ExpirationSettings" in data:
        import capo_chime_sdk_messaging.types.expiration_settings

        out["expiration_settings"] = (
            capo_chime_sdk_messaging.types.expiration_settings.deserialize_json(
                data["ExpirationSettings"]
            )
        )
    return out

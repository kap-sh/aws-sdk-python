"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#AppInstanceRetentionSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_identity.types.channel_retention_settings


class AppInstanceRetentionSettings(TypedDict):
    channel_retention_settings: NotRequired[
        "aws_sdk_chime_sdk_identity.types.channel_retention_settings.ChannelRetentionSettings"
    ]
    """<p>The length of time in days to retain the messages in a channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppInstanceRetentionSettings) -> dict:
    out: dict = {}
    if "channel_retention_settings" in value:
        import aws_sdk_chime_sdk_identity.types.channel_retention_settings

        out["ChannelRetentionSettings"] = (
            aws_sdk_chime_sdk_identity.types.channel_retention_settings.serialize_json(
                value["channel_retention_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> AppInstanceRetentionSettings:
    out: AppInstanceRetentionSettings = {}  # type: ignore[typeddict-item]
    if "ChannelRetentionSettings" in data:
        import aws_sdk_chime_sdk_identity.types.channel_retention_settings

        out["channel_retention_settings"] = (
            aws_sdk_chime_sdk_identity.types.channel_retention_settings.deserialize_json(
                data["ChannelRetentionSettings"]
            )
        )
    return out

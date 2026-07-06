"""Generated from Smithy shape ``com.amazonaws.medialive#LinkedChannelSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.follower_channel_settings
    import aws_sdk_medialive.types.primary_channel_settings


class LinkedChannelSettings(TypedDict, closed=True):
    follower_channel_settings: NotRequired[
        "aws_sdk_medialive.types.follower_channel_settings.FollowerChannelSettings"
    ]
    primary_channel_settings: NotRequired[
        "aws_sdk_medialive.types.primary_channel_settings.PrimaryChannelSettings"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: LinkedChannelSettings) -> dict:
    out: dict = {}
    if "follower_channel_settings" in value:
        import aws_sdk_medialive.types.follower_channel_settings

        out["followerChannelSettings"] = (
            aws_sdk_medialive.types.follower_channel_settings.serialize_json(
                value["follower_channel_settings"]
            )
        )
    if "primary_channel_settings" in value:
        import aws_sdk_medialive.types.primary_channel_settings

        out["primaryChannelSettings"] = (
            aws_sdk_medialive.types.primary_channel_settings.serialize_json(
                value["primary_channel_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> LinkedChannelSettings:
    out: LinkedChannelSettings = {}  # type: ignore[typeddict-item]
    if "followerChannelSettings" in data:
        import aws_sdk_medialive.types.follower_channel_settings

        out["follower_channel_settings"] = (
            aws_sdk_medialive.types.follower_channel_settings.deserialize_json(
                data["followerChannelSettings"]
            )
        )
    if "primaryChannelSettings" in data:
        import aws_sdk_medialive.types.primary_channel_settings

        out["primary_channel_settings"] = (
            aws_sdk_medialive.types.primary_channel_settings.deserialize_json(
                data["primaryChannelSettings"]
            )
        )
    return out

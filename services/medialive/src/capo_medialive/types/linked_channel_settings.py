"""Generated from Smithy shape ``com.amazonaws.medialive#LinkedChannelSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.follower_channel_settings
    import capo_medialive.types.primary_channel_settings


class LinkedChannelSettings(TypedDict, closed=True):
    follower_channel_settings: NotRequired[
        "capo_medialive.types.follower_channel_settings.FollowerChannelSettings"
    ]
    primary_channel_settings: NotRequired[
        "capo_medialive.types.primary_channel_settings.PrimaryChannelSettings"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: LinkedChannelSettings) -> dict:
    out: dict = {}
    if "follower_channel_settings" in value:
        import capo_medialive.types.follower_channel_settings

        out["followerChannelSettings"] = (
            capo_medialive.types.follower_channel_settings.serialize_json(
                value["follower_channel_settings"]
            )
        )
    if "primary_channel_settings" in value:
        import capo_medialive.types.primary_channel_settings

        out["primaryChannelSettings"] = (
            capo_medialive.types.primary_channel_settings.serialize_json(
                value["primary_channel_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> LinkedChannelSettings:
    out: LinkedChannelSettings = {}  # type: ignore[typeddict-item]
    if "followerChannelSettings" in data:
        import capo_medialive.types.follower_channel_settings

        out["follower_channel_settings"] = (
            capo_medialive.types.follower_channel_settings.deserialize_json(
                data["followerChannelSettings"]
            )
        )
    if "primaryChannelSettings" in data:
        import capo_medialive.types.primary_channel_settings

        out["primary_channel_settings"] = (
            capo_medialive.types.primary_channel_settings.deserialize_json(
                data["primaryChannelSettings"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.medialive#DescribeLinkedChannelSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.describe_follower_channel_settings
    import aws_sdk_medialive.types.describe_primary_channel_settings


class DescribeLinkedChannelSettings(TypedDict):
    follower_channel_settings: NotRequired[
        "aws_sdk_medialive.types.describe_follower_channel_settings.DescribeFollowerChannelSettings"
    ]
    primary_channel_settings: NotRequired[
        "aws_sdk_medialive.types.describe_primary_channel_settings.DescribePrimaryChannelSettings"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DescribeLinkedChannelSettings) -> dict:
    out: dict = {}
    if "follower_channel_settings" in value:
        import aws_sdk_medialive.types.describe_follower_channel_settings

        out["followerChannelSettings"] = (
            aws_sdk_medialive.types.describe_follower_channel_settings.serialize_json(
                value["follower_channel_settings"]
            )
        )
    if "primary_channel_settings" in value:
        import aws_sdk_medialive.types.describe_primary_channel_settings

        out["primaryChannelSettings"] = (
            aws_sdk_medialive.types.describe_primary_channel_settings.serialize_json(
                value["primary_channel_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeLinkedChannelSettings:
    out: DescribeLinkedChannelSettings = {}  # type: ignore[typeddict-item]
    if "followerChannelSettings" in data:
        import aws_sdk_medialive.types.describe_follower_channel_settings

        out["follower_channel_settings"] = (
            aws_sdk_medialive.types.describe_follower_channel_settings.deserialize_json(
                data["followerChannelSettings"]
            )
        )
    if "primaryChannelSettings" in data:
        import aws_sdk_medialive.types.describe_primary_channel_settings

        out["primary_channel_settings"] = (
            aws_sdk_medialive.types.describe_primary_channel_settings.deserialize_json(
                data["primaryChannelSettings"]
            )
        )
    return out

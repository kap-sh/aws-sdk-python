"""Generated from Smithy shape ``com.amazonaws.medialive#FollowerChannelSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.linked_channel_type


class FollowerChannelSettings(TypedDict, closed=True):
    linked_channel_type: NotRequired[
        "aws_sdk_medialive.types.linked_channel_type.LinkedChannelType"
    ]
    """Specifies this as a follower channel"""
    primary_channel_arn: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The ARN of the primary channel to follow"""


# --- restJson1 ser/de ---
def serialize_json(value: FollowerChannelSettings) -> dict:
    out: dict = {}
    if "linked_channel_type" in value:
        import aws_sdk_medialive.types.linked_channel_type

        out["linkedChannelType"] = (
            aws_sdk_medialive.types.linked_channel_type.serialize_json(
                value["linked_channel_type"]
            )
        )
    if "primary_channel_arn" in value:
        out["primaryChannelArn"] = value["primary_channel_arn"]
    return out


def deserialize_json(data: dict) -> FollowerChannelSettings:
    out: FollowerChannelSettings = {}  # type: ignore[typeddict-item]
    if "linkedChannelType" in data:
        import aws_sdk_medialive.types.linked_channel_type

        out["linked_channel_type"] = (
            aws_sdk_medialive.types.linked_channel_type.deserialize_json(
                data["linkedChannelType"]
            )
        )
    if "primaryChannelArn" in data:
        out["primary_channel_arn"] = data["primaryChannelArn"]
    return out

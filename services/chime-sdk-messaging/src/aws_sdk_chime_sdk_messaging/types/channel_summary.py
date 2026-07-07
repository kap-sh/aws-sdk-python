"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChannelSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.channel_mode
    import aws_sdk_chime_sdk_messaging.types.channel_privacy
    import aws_sdk_chime_sdk_messaging.types.chime_arn
    import aws_sdk_chime_sdk_messaging.types.metadata
    import aws_sdk_chime_sdk_messaging.types.non_empty_resource_name
    import aws_sdk_chime_sdk_messaging.types.timestamp


class ChannelSummary(TypedDict, closed=True):
    name: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.non_empty_resource_name.NonEmptyResourceName"
    ]
    """<p>The name of the channel.</p>"""
    channel_arn: NotRequired["aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"]
    """<p>The ARN of the channel.</p>"""
    mode: NotRequired["aws_sdk_chime_sdk_messaging.types.channel_mode.ChannelMode"]
    """<p>The mode of the channel.</p>"""
    privacy: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.channel_privacy.ChannelPrivacy"
    ]
    """<p>The privacy setting of the channel.</p>"""
    metadata: NotRequired["aws_sdk_chime_sdk_messaging.types.metadata.Metadata"]
    """<p>The metadata of the channel.</p>"""
    last_message_timestamp: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.timestamp.Timestamp"
    ]
    """<p>The time at which the last persistent message visible to the caller in a channel was sent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChannelSummary) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "channel_arn" in value:
        out["ChannelArn"] = value["channel_arn"]
    if "mode" in value:
        import aws_sdk_chime_sdk_messaging.types.channel_mode

        out["Mode"] = aws_sdk_chime_sdk_messaging.types.channel_mode.serialize_json(
            value["mode"]
        )
    if "privacy" in value:
        import aws_sdk_chime_sdk_messaging.types.channel_privacy

        out["Privacy"] = (
            aws_sdk_chime_sdk_messaging.types.channel_privacy.serialize_json(
                value["privacy"]
            )
        )
    if "metadata" in value:
        out["Metadata"] = value["metadata"]
    if "last_message_timestamp" in value:
        import aws_sdk_chime_sdk_messaging.types.timestamp

        out["LastMessageTimestamp"] = (
            aws_sdk_chime_sdk_messaging.types.timestamp.serialize_json(
                value["last_message_timestamp"]
            )
        )
    return out


def deserialize_json(data: dict) -> ChannelSummary:
    out: ChannelSummary = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "ChannelArn" in data:
        out["channel_arn"] = data["ChannelArn"]
    if "Mode" in data:
        import aws_sdk_chime_sdk_messaging.types.channel_mode

        out["mode"] = aws_sdk_chime_sdk_messaging.types.channel_mode.deserialize_json(
            data["Mode"]
        )
    if "Privacy" in data:
        import aws_sdk_chime_sdk_messaging.types.channel_privacy

        out["privacy"] = (
            aws_sdk_chime_sdk_messaging.types.channel_privacy.deserialize_json(
                data["Privacy"]
            )
        )
    if "Metadata" in data:
        out["metadata"] = data["Metadata"]
    if "LastMessageTimestamp" in data:
        import aws_sdk_chime_sdk_messaging.types.timestamp

        out["last_message_timestamp"] = (
            aws_sdk_chime_sdk_messaging.types.timestamp.deserialize_json(
                data["LastMessageTimestamp"]
            )
        )
    return out

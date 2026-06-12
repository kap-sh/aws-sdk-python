"""Generated from Smithy shape ``com.amazonaws.connect#MediaConcurrency``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.channel
    import aws_sdk_connect.types.concurrency
    import aws_sdk_connect.types.cross_channel_behavior


class MediaConcurrency(TypedDict):
    channel: "aws_sdk_connect.types.channel.Channel"
    """<p>The channels that agents can handle in the Contact Control Panel (CCP).</p>"""
    concurrency: "aws_sdk_connect.types.concurrency.Concurrency"
    """<p>The number of contacts an agent can have on a channel simultaneously.</p> <p>Valid Range for <code>VOICE</code>: Minimum value of 1. Maximum value of 1.</p> <p>Valid Range for <code>CHAT</code>: Minimum value of 1. Maximum value of 10.</p> <p>Valid Range for <code>TASK</code>: Minimum value of 1. Maximum value of 10.</p>"""
    cross_channel_behavior: NotRequired[
        "aws_sdk_connect.types.cross_channel_behavior.CrossChannelBehavior"
    ]
    """<p>Defines the cross-channel routing behavior for each channel that is enabled for this Routing Profile. For example, this allows you to offer an agent a different contact from another channel when they are currently working with a contact from a Voice channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MediaConcurrency) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.channel

    out["Channel"] = aws_sdk_connect.types.channel.serialize_json(value["channel"])
    out["Concurrency"] = value["concurrency"]
    if "cross_channel_behavior" in value:
        import aws_sdk_connect.types.cross_channel_behavior

        out["CrossChannelBehavior"] = (
            aws_sdk_connect.types.cross_channel_behavior.serialize_json(
                value["cross_channel_behavior"]
            )
        )
    return out


def deserialize_json(data: dict) -> MediaConcurrency:
    out: MediaConcurrency = {}  # type: ignore[typeddict-item]
    if "Channel" in data:
        import aws_sdk_connect.types.channel

        out["channel"] = aws_sdk_connect.types.channel.deserialize_json(data["Channel"])
    else:
        raise DeserializationError("MediaConcurrency.channel required")
    if "Concurrency" in data:
        out["concurrency"] = data["Concurrency"]
    else:
        raise DeserializationError("MediaConcurrency.concurrency required")
    if "CrossChannelBehavior" in data:
        import aws_sdk_connect.types.cross_channel_behavior

        out["cross_channel_behavior"] = (
            aws_sdk_connect.types.cross_channel_behavior.deserialize_json(
                data["CrossChannelBehavior"]
            )
        )
    return out

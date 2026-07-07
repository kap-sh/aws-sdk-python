"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#GetChannelMessageResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.channel_message


class GetChannelMessageResponse(TypedDict, closed=True):
    channel_message: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.channel_message.ChannelMessage"
    ]
    """<p>The details of and content in the message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetChannelMessageResponse) -> dict:
    out: dict = {}
    if "channel_message" in value:
        import aws_sdk_chime_sdk_messaging.types.channel_message

        out["ChannelMessage"] = (
            aws_sdk_chime_sdk_messaging.types.channel_message.serialize_json(
                value["channel_message"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetChannelMessageResponse:
    out: GetChannelMessageResponse = {}  # type: ignore[typeddict-item]
    if "ChannelMessage" in data:
        import aws_sdk_chime_sdk_messaging.types.channel_message

        out["channel_message"] = (
            aws_sdk_chime_sdk_messaging.types.channel_message.deserialize_json(
                data["ChannelMessage"]
            )
        )
    return out

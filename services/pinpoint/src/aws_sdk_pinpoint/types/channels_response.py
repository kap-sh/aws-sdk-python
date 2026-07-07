"""Generated from Smithy shape ``com.amazonaws.pinpoint#ChannelsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.map_of_channel_response


class ChannelsResponse(TypedDict, closed=True):
    channels: NotRequired[
        "aws_sdk_pinpoint.types.map_of_channel_response.MapOfChannelResponse"
    ]
    """<p>A map that contains a multipart response for each channel. For each item in this object, the ChannelType is the key and the Channel is the value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChannelsResponse) -> dict:
    out: dict = {}
    if "channels" in value:
        import aws_sdk_pinpoint.types.map_of_channel_response

        out["Channels"] = aws_sdk_pinpoint.types.map_of_channel_response.serialize_json(
            value["channels"]
        )
    return out


def deserialize_json(data: dict) -> ChannelsResponse:
    out: ChannelsResponse = {}  # type: ignore[typeddict-item]
    if "Channels" in data:
        import aws_sdk_pinpoint.types.map_of_channel_response

        out["channels"] = (
            aws_sdk_pinpoint.types.map_of_channel_response.deserialize_json(
                data["Channels"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetVoiceChannelResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.voice_channel_response


class GetVoiceChannelResponse(TypedDict):
    voice_channel_response: NotRequired[
        "aws_sdk_pinpoint.types.voice_channel_response.VoiceChannelResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetVoiceChannelResponse) -> dict:
    out: dict = {}
    if "voice_channel_response" in value:
        import aws_sdk_pinpoint.types.voice_channel_response

        out["VoiceChannelResponse"] = (
            aws_sdk_pinpoint.types.voice_channel_response.serialize_json(
                value["voice_channel_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetVoiceChannelResponse:
    out: GetVoiceChannelResponse = {}  # type: ignore[typeddict-item]
    if "VoiceChannelResponse" in data:
        import aws_sdk_pinpoint.types.voice_channel_response

        out["voice_channel_response"] = (
            aws_sdk_pinpoint.types.voice_channel_response.deserialize_json(
                data["VoiceChannelResponse"]
            )
        )
    return out

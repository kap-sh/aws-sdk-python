"""Generated from Smithy shape ``com.amazonaws.pinpoint#UpdateVoiceChannelRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.voice_channel_request


class UpdateVoiceChannelRequest(TypedDict):
    application_id: "aws_sdk_pinpoint.types.__string.__string"
    """<p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>"""
    voice_channel_request: NotRequired[
        "aws_sdk_pinpoint.types.voice_channel_request.VoiceChannelRequest"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateVoiceChannelRequest) -> dict:
    out: dict = {}
    if "voice_channel_request" in value:
        import aws_sdk_pinpoint.types.voice_channel_request

        out["VoiceChannelRequest"] = (
            aws_sdk_pinpoint.types.voice_channel_request.serialize_json(
                value["voice_channel_request"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateVoiceChannelRequest:
    out: UpdateVoiceChannelRequest = {}  # type: ignore[typeddict-item]
    if "VoiceChannelRequest" in data:
        import aws_sdk_pinpoint.types.voice_channel_request

        out["voice_channel_request"] = (
            aws_sdk_pinpoint.types.voice_channel_request.deserialize_json(
                data["VoiceChannelRequest"]
            )
        )
    return out

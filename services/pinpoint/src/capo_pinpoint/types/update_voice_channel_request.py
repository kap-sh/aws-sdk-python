"""Generated from Smithy shape ``com.amazonaws.pinpoint#UpdateVoiceChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.voice_channel_request


class UpdateVoiceChannelRequest(TypedDict, closed=True):
    application_id: "capo_pinpoint.types.__string.__string"
    """<p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>"""
    voice_channel_request: NotRequired[
        "capo_pinpoint.types.voice_channel_request.VoiceChannelRequest"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateVoiceChannelRequest) -> dict:
    out: dict = {}
    if "voice_channel_request" in value:
        import capo_pinpoint.types.voice_channel_request

        out["VoiceChannelRequest"] = (
            capo_pinpoint.types.voice_channel_request.serialize_json(
                value["voice_channel_request"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateVoiceChannelRequest:
    out: UpdateVoiceChannelRequest = {}  # type: ignore[typeddict-item]
    if "VoiceChannelRequest" in data:
        import capo_pinpoint.types.voice_channel_request

        out["voice_channel_request"] = (
            capo_pinpoint.types.voice_channel_request.deserialize_json(
                data["VoiceChannelRequest"]
            )
        )
    return out

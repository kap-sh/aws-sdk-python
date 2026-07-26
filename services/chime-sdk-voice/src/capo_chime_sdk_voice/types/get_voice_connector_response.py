"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#GetVoiceConnectorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.voice_connector


class GetVoiceConnectorResponse(TypedDict, closed=True):
    voice_connector: NotRequired[
        "capo_chime_sdk_voice.types.voice_connector.VoiceConnector"
    ]
    """<p>The Voice Connector details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetVoiceConnectorResponse) -> dict:
    out: dict = {}
    if "voice_connector" in value:
        import capo_chime_sdk_voice.types.voice_connector

        out["VoiceConnector"] = (
            capo_chime_sdk_voice.types.voice_connector.serialize_json(
                value["voice_connector"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetVoiceConnectorResponse:
    out: GetVoiceConnectorResponse = {}  # type: ignore[typeddict-item]
    if "VoiceConnector" in data:
        import capo_chime_sdk_voice.types.voice_connector

        out["voice_connector"] = (
            capo_chime_sdk_voice.types.voice_connector.deserialize_json(
                data["VoiceConnector"]
            )
        )
    return out

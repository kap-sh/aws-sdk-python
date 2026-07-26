"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#CreateVoiceConnectorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.voice_connector


class CreateVoiceConnectorResponse(TypedDict, closed=True):
    voice_connector: NotRequired[
        "capo_chime_sdk_voice.types.voice_connector.VoiceConnector"
    ]
    """<p>The details of the Voice Connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateVoiceConnectorResponse) -> dict:
    out: dict = {}
    if "voice_connector" in value:
        import capo_chime_sdk_voice.types.voice_connector

        out["VoiceConnector"] = (
            capo_chime_sdk_voice.types.voice_connector.serialize_json(
                value["voice_connector"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateVoiceConnectorResponse:
    out: CreateVoiceConnectorResponse = {}  # type: ignore[typeddict-item]
    if "VoiceConnector" in data:
        import capo_chime_sdk_voice.types.voice_connector

        out["voice_connector"] = (
            capo_chime_sdk_voice.types.voice_connector.deserialize_json(
                data["VoiceConnector"]
            )
        )
    return out

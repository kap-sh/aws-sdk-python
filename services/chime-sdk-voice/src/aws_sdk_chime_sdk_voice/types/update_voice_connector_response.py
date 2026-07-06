"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#UpdateVoiceConnectorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.voice_connector


class UpdateVoiceConnectorResponse(TypedDict, closed=True):
    voice_connector: NotRequired[
        "aws_sdk_chime_sdk_voice.types.voice_connector.VoiceConnector"
    ]
    """<p>The updated Voice Connector details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateVoiceConnectorResponse) -> dict:
    out: dict = {}
    if "voice_connector" in value:
        import aws_sdk_chime_sdk_voice.types.voice_connector

        out["VoiceConnector"] = (
            aws_sdk_chime_sdk_voice.types.voice_connector.serialize_json(
                value["voice_connector"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateVoiceConnectorResponse:
    out: UpdateVoiceConnectorResponse = {}  # type: ignore[typeddict-item]
    if "VoiceConnector" in data:
        import aws_sdk_chime_sdk_voice.types.voice_connector

        out["voice_connector"] = (
            aws_sdk_chime_sdk_voice.types.voice_connector.deserialize_json(
                data["VoiceConnector"]
            )
        )
    return out

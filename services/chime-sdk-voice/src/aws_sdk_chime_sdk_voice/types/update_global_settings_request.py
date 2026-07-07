"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#UpdateGlobalSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.voice_connector_settings


class UpdateGlobalSettingsRequest(TypedDict, closed=True):
    voice_connector: NotRequired[
        "aws_sdk_chime_sdk_voice.types.voice_connector_settings.VoiceConnectorSettings"
    ]
    """<p>The Voice Connector settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGlobalSettingsRequest) -> dict:
    out: dict = {}
    if "voice_connector" in value:
        import aws_sdk_chime_sdk_voice.types.voice_connector_settings

        out["VoiceConnector"] = (
            aws_sdk_chime_sdk_voice.types.voice_connector_settings.serialize_json(
                value["voice_connector"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateGlobalSettingsRequest:
    out: UpdateGlobalSettingsRequest = {}  # type: ignore[typeddict-item]
    if "VoiceConnector" in data:
        import aws_sdk_chime_sdk_voice.types.voice_connector_settings

        out["voice_connector"] = (
            aws_sdk_chime_sdk_voice.types.voice_connector_settings.deserialize_json(
                data["VoiceConnector"]
            )
        )
    return out

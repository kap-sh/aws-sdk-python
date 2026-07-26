"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#GetGlobalSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.voice_connector_settings


class GetGlobalSettingsResponse(TypedDict, closed=True):
    voice_connector: NotRequired[
        "capo_chime_sdk_voice.types.voice_connector_settings.VoiceConnectorSettings"
    ]
    """<p>The Voice Connector settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGlobalSettingsResponse) -> dict:
    out: dict = {}
    if "voice_connector" in value:
        import capo_chime_sdk_voice.types.voice_connector_settings

        out["VoiceConnector"] = (
            capo_chime_sdk_voice.types.voice_connector_settings.serialize_json(
                value["voice_connector"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetGlobalSettingsResponse:
    out: GetGlobalSettingsResponse = {}  # type: ignore[typeddict-item]
    if "VoiceConnector" in data:
        import capo_chime_sdk_voice.types.voice_connector_settings

        out["voice_connector"] = (
            capo_chime_sdk_voice.types.voice_connector_settings.deserialize_json(
                data["VoiceConnector"]
            )
        )
    return out

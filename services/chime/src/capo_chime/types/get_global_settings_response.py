"""Generated from Smithy shape ``com.amazonaws.chime#GetGlobalSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime.types.business_calling_settings
    import capo_chime.types.voice_connector_settings


class GetGlobalSettingsResponse(TypedDict, closed=True):
    business_calling: NotRequired[
        "capo_chime.types.business_calling_settings.BusinessCallingSettings"
    ]
    """<p>The Amazon Chime Business Calling settings.</p>"""
    voice_connector: NotRequired[
        "capo_chime.types.voice_connector_settings.VoiceConnectorSettings"
    ]
    """<p>The Amazon Chime Voice Connector settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGlobalSettingsResponse) -> dict:
    out: dict = {}
    if "business_calling" in value:
        import capo_chime.types.business_calling_settings

        out["BusinessCalling"] = (
            capo_chime.types.business_calling_settings.serialize_json(
                value["business_calling"]
            )
        )
    if "voice_connector" in value:
        import capo_chime.types.voice_connector_settings

        out["VoiceConnector"] = (
            capo_chime.types.voice_connector_settings.serialize_json(
                value["voice_connector"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetGlobalSettingsResponse:
    out: GetGlobalSettingsResponse = {}  # type: ignore[typeddict-item]
    if "BusinessCalling" in data:
        import capo_chime.types.business_calling_settings

        out["business_calling"] = (
            capo_chime.types.business_calling_settings.deserialize_json(
                data["BusinessCalling"]
            )
        )
    if "VoiceConnector" in data:
        import capo_chime.types.voice_connector_settings

        out["voice_connector"] = (
            capo_chime.types.voice_connector_settings.deserialize_json(
                data["VoiceConnector"]
            )
        )
    return out

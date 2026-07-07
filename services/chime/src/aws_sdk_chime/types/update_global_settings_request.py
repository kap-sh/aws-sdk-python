"""Generated from Smithy shape ``com.amazonaws.chime#UpdateGlobalSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime.types.business_calling_settings
    import aws_sdk_chime.types.voice_connector_settings


class UpdateGlobalSettingsRequest(TypedDict, closed=True):
    business_calling: NotRequired[
        "aws_sdk_chime.types.business_calling_settings.BusinessCallingSettings"
    ]
    """<p>The Amazon Chime Business Calling settings.</p>"""
    voice_connector: NotRequired[
        "aws_sdk_chime.types.voice_connector_settings.VoiceConnectorSettings"
    ]
    """<p>The Amazon Chime Voice Connector settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGlobalSettingsRequest) -> dict:
    out: dict = {}
    if "business_calling" in value:
        import aws_sdk_chime.types.business_calling_settings

        out["BusinessCalling"] = (
            aws_sdk_chime.types.business_calling_settings.serialize_json(
                value["business_calling"]
            )
        )
    if "voice_connector" in value:
        import aws_sdk_chime.types.voice_connector_settings

        out["VoiceConnector"] = (
            aws_sdk_chime.types.voice_connector_settings.serialize_json(
                value["voice_connector"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateGlobalSettingsRequest:
    out: UpdateGlobalSettingsRequest = {}  # type: ignore[typeddict-item]
    if "BusinessCalling" in data:
        import aws_sdk_chime.types.business_calling_settings

        out["business_calling"] = (
            aws_sdk_chime.types.business_calling_settings.deserialize_json(
                data["BusinessCalling"]
            )
        )
    if "VoiceConnector" in data:
        import aws_sdk_chime.types.voice_connector_settings

        out["voice_connector"] = (
            aws_sdk_chime.types.voice_connector_settings.deserialize_json(
                data["VoiceConnector"]
            )
        )
    return out

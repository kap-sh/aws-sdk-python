"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#GetVoiceConnectorEmergencyCallingConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.non_empty_string


class GetVoiceConnectorEmergencyCallingConfigurationRequest(TypedDict, closed=True):
    voice_connector_id: "capo_chime_sdk_voice.types.non_empty_string.NonEmptyString"
    """<p>The Voice Connector ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: GetVoiceConnectorEmergencyCallingConfigurationRequest,
) -> dict:
    out: dict = {}
    return out


def deserialize_json(
    data: dict,
) -> GetVoiceConnectorEmergencyCallingConfigurationRequest:
    out: GetVoiceConnectorEmergencyCallingConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out

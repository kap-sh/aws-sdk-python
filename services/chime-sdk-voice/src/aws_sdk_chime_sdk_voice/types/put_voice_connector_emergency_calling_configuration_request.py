"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#PutVoiceConnectorEmergencyCallingConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_chime_sdk_voice.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.emergency_calling_configuration
    import aws_sdk_chime_sdk_voice.types.non_empty_string


class PutVoiceConnectorEmergencyCallingConfigurationRequest(TypedDict, closed=True):
    voice_connector_id: "aws_sdk_chime_sdk_voice.types.non_empty_string.NonEmptyString"
    """<p>The Voice Connector ID.</p>"""
    emergency_calling_configuration: "aws_sdk_chime_sdk_voice.types.emergency_calling_configuration.EmergencyCallingConfiguration"
    """<p>The configuration being updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: PutVoiceConnectorEmergencyCallingConfigurationRequest,
) -> dict:
    out: dict = {}
    import aws_sdk_chime_sdk_voice.types.emergency_calling_configuration

    out["EmergencyCallingConfiguration"] = (
        aws_sdk_chime_sdk_voice.types.emergency_calling_configuration.serialize_json(
            value["emergency_calling_configuration"]
        )
    )
    return out


def deserialize_json(
    data: dict,
) -> PutVoiceConnectorEmergencyCallingConfigurationRequest:
    out: PutVoiceConnectorEmergencyCallingConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "EmergencyCallingConfiguration" in data:
        import aws_sdk_chime_sdk_voice.types.emergency_calling_configuration

        out["emergency_calling_configuration"] = (
            aws_sdk_chime_sdk_voice.types.emergency_calling_configuration.deserialize_json(
                data["EmergencyCallingConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "PutVoiceConnectorEmergencyCallingConfigurationRequest.emergency_calling_configuration required"
        )
    return out

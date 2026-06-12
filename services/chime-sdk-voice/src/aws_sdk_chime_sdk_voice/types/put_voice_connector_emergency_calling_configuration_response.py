"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#PutVoiceConnectorEmergencyCallingConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.emergency_calling_configuration


class PutVoiceConnectorEmergencyCallingConfigurationResponse(TypedDict):
    emergency_calling_configuration: NotRequired[
        "aws_sdk_chime_sdk_voice.types.emergency_calling_configuration.EmergencyCallingConfiguration"
    ]
    """<p>The updated configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: PutVoiceConnectorEmergencyCallingConfigurationResponse,
) -> dict:
    out: dict = {}
    if "emergency_calling_configuration" in value:
        import aws_sdk_chime_sdk_voice.types.emergency_calling_configuration

        out["EmergencyCallingConfiguration"] = (
            aws_sdk_chime_sdk_voice.types.emergency_calling_configuration.serialize_json(
                value["emergency_calling_configuration"]
            )
        )
    return out


def deserialize_json(
    data: dict,
) -> PutVoiceConnectorEmergencyCallingConfigurationResponse:
    out: PutVoiceConnectorEmergencyCallingConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "EmergencyCallingConfiguration" in data:
        import aws_sdk_chime_sdk_voice.types.emergency_calling_configuration

        out["emergency_calling_configuration"] = (
            aws_sdk_chime_sdk_voice.types.emergency_calling_configuration.deserialize_json(
                data["EmergencyCallingConfiguration"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#DNISEmergencyCallingConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.dnis_emergency_calling_configuration

DNISEmergencyCallingConfigurationList: TypeAlias = list[
    "capo_chime_sdk_voice.types.dnis_emergency_calling_configuration.DNISEmergencyCallingConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: DNISEmergencyCallingConfigurationList) -> list:
    import capo_chime_sdk_voice.types.dnis_emergency_calling_configuration

    out: list = []
    for item in value:
        out.append(
            capo_chime_sdk_voice.types.dnis_emergency_calling_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DNISEmergencyCallingConfigurationList:
    import capo_chime_sdk_voice.types.dnis_emergency_calling_configuration

    out: DNISEmergencyCallingConfigurationList = []
    for item in data:
        out.append(
            capo_chime_sdk_voice.types.dnis_emergency_calling_configuration.deserialize_json(
                item
            )
        )
    return out

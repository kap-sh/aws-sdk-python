"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#EmergencyCallingConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.dnis_emergency_calling_configuration_list


class EmergencyCallingConfiguration(TypedDict):
    dnis: NotRequired[
        "aws_sdk_chime_sdk_voice.types.dnis_emergency_calling_configuration_list.DNISEmergencyCallingConfigurationList"
    ]
    """<p>The Dialed Number Identification Service (DNIS) emergency calling configuration details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EmergencyCallingConfiguration) -> dict:
    out: dict = {}
    if "dnis" in value:
        import aws_sdk_chime_sdk_voice.types.dnis_emergency_calling_configuration_list

        out["DNIS"] = (
            aws_sdk_chime_sdk_voice.types.dnis_emergency_calling_configuration_list.serialize_json(
                value["dnis"]
            )
        )
    return out


def deserialize_json(data: dict) -> EmergencyCallingConfiguration:
    out: EmergencyCallingConfiguration = {}  # type: ignore[typeddict-item]
    if "DNIS" in data:
        import aws_sdk_chime_sdk_voice.types.dnis_emergency_calling_configuration_list

        out["dnis"] = (
            aws_sdk_chime_sdk_voice.types.dnis_emergency_calling_configuration_list.deserialize_json(
                data["DNIS"]
            )
        )
    return out

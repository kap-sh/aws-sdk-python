"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#PutVoiceConnectorExternalSystemsConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.external_systems_configuration


class PutVoiceConnectorExternalSystemsConfigurationResponse(TypedDict, closed=True):
    external_systems_configuration: NotRequired[
        "aws_sdk_chime_sdk_voice.types.external_systems_configuration.ExternalSystemsConfiguration"
    ]
    """<p>An object that contains information about an external systems configuration for a Voice Connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: PutVoiceConnectorExternalSystemsConfigurationResponse,
) -> dict:
    out: dict = {}
    if "external_systems_configuration" in value:
        import aws_sdk_chime_sdk_voice.types.external_systems_configuration

        out["ExternalSystemsConfiguration"] = (
            aws_sdk_chime_sdk_voice.types.external_systems_configuration.serialize_json(
                value["external_systems_configuration"]
            )
        )
    return out


def deserialize_json(
    data: dict,
) -> PutVoiceConnectorExternalSystemsConfigurationResponse:
    out: PutVoiceConnectorExternalSystemsConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "ExternalSystemsConfiguration" in data:
        import aws_sdk_chime_sdk_voice.types.external_systems_configuration

        out["external_systems_configuration"] = (
            aws_sdk_chime_sdk_voice.types.external_systems_configuration.deserialize_json(
                data["ExternalSystemsConfiguration"]
            )
        )
    return out

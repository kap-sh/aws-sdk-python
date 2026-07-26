"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#PutVoiceConnectorLoggingConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.logging_configuration


class PutVoiceConnectorLoggingConfigurationResponse(TypedDict, closed=True):
    logging_configuration: NotRequired[
        "capo_chime_sdk_voice.types.logging_configuration.LoggingConfiguration"
    ]
    """<p>The updated logging configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutVoiceConnectorLoggingConfigurationResponse) -> dict:
    out: dict = {}
    if "logging_configuration" in value:
        import capo_chime_sdk_voice.types.logging_configuration

        out["LoggingConfiguration"] = (
            capo_chime_sdk_voice.types.logging_configuration.serialize_json(
                value["logging_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutVoiceConnectorLoggingConfigurationResponse:
    out: PutVoiceConnectorLoggingConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "LoggingConfiguration" in data:
        import capo_chime_sdk_voice.types.logging_configuration

        out["logging_configuration"] = (
            capo_chime_sdk_voice.types.logging_configuration.deserialize_json(
                data["LoggingConfiguration"]
            )
        )
    return out

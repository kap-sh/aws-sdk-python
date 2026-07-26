"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#GetVoiceConnectorLoggingConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.logging_configuration


class GetVoiceConnectorLoggingConfigurationResponse(TypedDict, closed=True):
    logging_configuration: NotRequired[
        "capo_chime_sdk_voice.types.logging_configuration.LoggingConfiguration"
    ]
    """<p>The logging configuration details .</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetVoiceConnectorLoggingConfigurationResponse) -> dict:
    out: dict = {}
    if "logging_configuration" in value:
        import capo_chime_sdk_voice.types.logging_configuration

        out["LoggingConfiguration"] = (
            capo_chime_sdk_voice.types.logging_configuration.serialize_json(
                value["logging_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetVoiceConnectorLoggingConfigurationResponse:
    out: GetVoiceConnectorLoggingConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "LoggingConfiguration" in data:
        import capo_chime_sdk_voice.types.logging_configuration

        out["logging_configuration"] = (
            capo_chime_sdk_voice.types.logging_configuration.deserialize_json(
                data["LoggingConfiguration"]
            )
        )
    return out

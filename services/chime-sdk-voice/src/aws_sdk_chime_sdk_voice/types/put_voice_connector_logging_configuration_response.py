"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#PutVoiceConnectorLoggingConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.logging_configuration


class PutVoiceConnectorLoggingConfigurationResponse(TypedDict):
    logging_configuration: NotRequired[
        "aws_sdk_chime_sdk_voice.types.logging_configuration.LoggingConfiguration"
    ]
    """<p>The updated logging configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutVoiceConnectorLoggingConfigurationResponse) -> dict:
    out: dict = {}
    if "logging_configuration" in value:
        import aws_sdk_chime_sdk_voice.types.logging_configuration

        out["LoggingConfiguration"] = (
            aws_sdk_chime_sdk_voice.types.logging_configuration.serialize_json(
                value["logging_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutVoiceConnectorLoggingConfigurationResponse:
    out: PutVoiceConnectorLoggingConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "LoggingConfiguration" in data:
        import aws_sdk_chime_sdk_voice.types.logging_configuration

        out["logging_configuration"] = (
            aws_sdk_chime_sdk_voice.types.logging_configuration.deserialize_json(
                data["LoggingConfiguration"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#PutVoiceConnectorLoggingConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_chime_sdk_voice.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.logging_configuration
    import capo_chime_sdk_voice.types.non_empty_string


class PutVoiceConnectorLoggingConfigurationRequest(TypedDict, closed=True):
    voice_connector_id: "capo_chime_sdk_voice.types.non_empty_string.NonEmptyString"
    """<p>The Voice Connector ID.</p>"""
    logging_configuration: (
        "capo_chime_sdk_voice.types.logging_configuration.LoggingConfiguration"
    )
    """<p>The logging configuration being updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutVoiceConnectorLoggingConfigurationRequest) -> dict:
    out: dict = {}
    import capo_chime_sdk_voice.types.logging_configuration

    out["LoggingConfiguration"] = (
        capo_chime_sdk_voice.types.logging_configuration.serialize_json(
            value["logging_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutVoiceConnectorLoggingConfigurationRequest:
    out: PutVoiceConnectorLoggingConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "LoggingConfiguration" in data:
        import capo_chime_sdk_voice.types.logging_configuration

        out["logging_configuration"] = (
            capo_chime_sdk_voice.types.logging_configuration.deserialize_json(
                data["LoggingConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "PutVoiceConnectorLoggingConfigurationRequest.logging_configuration required"
        )
    return out

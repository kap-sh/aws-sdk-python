"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#PutVoiceConnectorStreamingConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_chime_sdk_voice.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.non_empty_string
    import aws_sdk_chime_sdk_voice.types.streaming_configuration


class PutVoiceConnectorStreamingConfigurationRequest(TypedDict, closed=True):
    voice_connector_id: "aws_sdk_chime_sdk_voice.types.non_empty_string.NonEmptyString"
    """<p>The Voice Connector ID.</p>"""
    streaming_configuration: (
        "aws_sdk_chime_sdk_voice.types.streaming_configuration.StreamingConfiguration"
    )
    """<p>The streaming settings being updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutVoiceConnectorStreamingConfigurationRequest) -> dict:
    out: dict = {}
    import aws_sdk_chime_sdk_voice.types.streaming_configuration

    out["StreamingConfiguration"] = (
        aws_sdk_chime_sdk_voice.types.streaming_configuration.serialize_json(
            value["streaming_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutVoiceConnectorStreamingConfigurationRequest:
    out: PutVoiceConnectorStreamingConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "StreamingConfiguration" in data:
        import aws_sdk_chime_sdk_voice.types.streaming_configuration

        out["streaming_configuration"] = (
            aws_sdk_chime_sdk_voice.types.streaming_configuration.deserialize_json(
                data["StreamingConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "PutVoiceConnectorStreamingConfigurationRequest.streaming_configuration required"
        )
    return out

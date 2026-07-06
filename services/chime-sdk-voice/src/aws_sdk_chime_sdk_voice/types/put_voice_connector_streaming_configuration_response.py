"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#PutVoiceConnectorStreamingConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.streaming_configuration


class PutVoiceConnectorStreamingConfigurationResponse(TypedDict, closed=True):
    streaming_configuration: NotRequired[
        "aws_sdk_chime_sdk_voice.types.streaming_configuration.StreamingConfiguration"
    ]
    """<p>The updated streaming settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutVoiceConnectorStreamingConfigurationResponse) -> dict:
    out: dict = {}
    if "streaming_configuration" in value:
        import aws_sdk_chime_sdk_voice.types.streaming_configuration

        out["StreamingConfiguration"] = (
            aws_sdk_chime_sdk_voice.types.streaming_configuration.serialize_json(
                value["streaming_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutVoiceConnectorStreamingConfigurationResponse:
    out: PutVoiceConnectorStreamingConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "StreamingConfiguration" in data:
        import aws_sdk_chime_sdk_voice.types.streaming_configuration

        out["streaming_configuration"] = (
            aws_sdk_chime_sdk_voice.types.streaming_configuration.deserialize_json(
                data["StreamingConfiguration"]
            )
        )
    return out

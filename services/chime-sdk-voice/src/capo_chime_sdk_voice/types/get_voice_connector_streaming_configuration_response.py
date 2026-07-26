"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#GetVoiceConnectorStreamingConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.streaming_configuration


class GetVoiceConnectorStreamingConfigurationResponse(TypedDict, closed=True):
    streaming_configuration: NotRequired[
        "capo_chime_sdk_voice.types.streaming_configuration.StreamingConfiguration"
    ]
    """<p>The details of the streaming configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetVoiceConnectorStreamingConfigurationResponse) -> dict:
    out: dict = {}
    if "streaming_configuration" in value:
        import capo_chime_sdk_voice.types.streaming_configuration

        out["StreamingConfiguration"] = (
            capo_chime_sdk_voice.types.streaming_configuration.serialize_json(
                value["streaming_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetVoiceConnectorStreamingConfigurationResponse:
    out: GetVoiceConnectorStreamingConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "StreamingConfiguration" in data:
        import capo_chime_sdk_voice.types.streaming_configuration

        out["streaming_configuration"] = (
            capo_chime_sdk_voice.types.streaming_configuration.deserialize_json(
                data["StreamingConfiguration"]
            )
        )
    return out

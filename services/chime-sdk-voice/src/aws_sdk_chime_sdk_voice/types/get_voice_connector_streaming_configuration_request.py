"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#GetVoiceConnectorStreamingConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.non_empty_string


class GetVoiceConnectorStreamingConfigurationRequest(TypedDict, closed=True):
    voice_connector_id: "aws_sdk_chime_sdk_voice.types.non_empty_string.NonEmptyString"
    """<p>The Voice Connector ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetVoiceConnectorStreamingConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetVoiceConnectorStreamingConfigurationRequest:
    out: GetVoiceConnectorStreamingConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out

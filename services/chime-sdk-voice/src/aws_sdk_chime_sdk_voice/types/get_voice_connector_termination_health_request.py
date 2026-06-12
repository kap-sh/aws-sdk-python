"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#GetVoiceConnectorTerminationHealthRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.non_empty_string


class GetVoiceConnectorTerminationHealthRequest(TypedDict):
    voice_connector_id: "aws_sdk_chime_sdk_voice.types.non_empty_string.NonEmptyString"
    """<p>The Voice Connector ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetVoiceConnectorTerminationHealthRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetVoiceConnectorTerminationHealthRequest:
    out: GetVoiceConnectorTerminationHealthRequest = {}  # type: ignore[typeddict-item]
    return out

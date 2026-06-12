"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#GetVoiceConnectorProxyRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.non_empty_string128


class GetVoiceConnectorProxyRequest(TypedDict):
    voice_connector_id: (
        "aws_sdk_chime_sdk_voice.types.non_empty_string128.NonEmptyString128"
    )
    """<p>The Voice Connector ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetVoiceConnectorProxyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetVoiceConnectorProxyRequest:
    out: GetVoiceConnectorProxyRequest = {}  # type: ignore[typeddict-item]
    return out

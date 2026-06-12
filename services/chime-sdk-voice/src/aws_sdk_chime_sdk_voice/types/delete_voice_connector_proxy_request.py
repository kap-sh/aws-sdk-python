"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#DeleteVoiceConnectorProxyRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.non_empty_string128


class DeleteVoiceConnectorProxyRequest(TypedDict):
    voice_connector_id: (
        "aws_sdk_chime_sdk_voice.types.non_empty_string128.NonEmptyString128"
    )
    """<p>The Voice Connector ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteVoiceConnectorProxyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteVoiceConnectorProxyRequest:
    out: DeleteVoiceConnectorProxyRequest = {}  # type: ignore[typeddict-item]
    return out

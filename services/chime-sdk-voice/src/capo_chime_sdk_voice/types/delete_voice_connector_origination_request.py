"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#DeleteVoiceConnectorOriginationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.non_empty_string


class DeleteVoiceConnectorOriginationRequest(TypedDict, closed=True):
    voice_connector_id: "capo_chime_sdk_voice.types.non_empty_string.NonEmptyString"
    """<p>The Voice Connector ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteVoiceConnectorOriginationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteVoiceConnectorOriginationRequest:
    out: DeleteVoiceConnectorOriginationRequest = {}  # type: ignore[typeddict-item]
    return out

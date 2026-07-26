"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#DeleteVoiceConnectorProxyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.non_empty_string128


class DeleteVoiceConnectorProxyRequest(TypedDict, closed=True):
    voice_connector_id: (
        "capo_chime_sdk_voice.types.non_empty_string128.NonEmptyString128"
    )
    """<p>The Voice Connector ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteVoiceConnectorProxyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteVoiceConnectorProxyRequest:
    out: DeleteVoiceConnectorProxyRequest = {}  # type: ignore[typeddict-item]
    return out

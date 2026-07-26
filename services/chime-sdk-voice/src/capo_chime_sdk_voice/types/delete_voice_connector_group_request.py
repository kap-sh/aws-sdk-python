"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#DeleteVoiceConnectorGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.non_empty_string


class DeleteVoiceConnectorGroupRequest(TypedDict, closed=True):
    voice_connector_group_id: (
        "capo_chime_sdk_voice.types.non_empty_string.NonEmptyString"
    )
    """<p>The Voice Connector Group ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteVoiceConnectorGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteVoiceConnectorGroupRequest:
    out: DeleteVoiceConnectorGroupRequest = {}  # type: ignore[typeddict-item]
    return out

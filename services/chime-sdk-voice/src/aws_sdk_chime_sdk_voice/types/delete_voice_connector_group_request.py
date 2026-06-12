"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#DeleteVoiceConnectorGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.non_empty_string


class DeleteVoiceConnectorGroupRequest(TypedDict):
    voice_connector_group_id: (
        "aws_sdk_chime_sdk_voice.types.non_empty_string.NonEmptyString"
    )
    """<p>The Voice Connector Group ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteVoiceConnectorGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteVoiceConnectorGroupRequest:
    out: DeleteVoiceConnectorGroupRequest = {}  # type: ignore[typeddict-item]
    return out

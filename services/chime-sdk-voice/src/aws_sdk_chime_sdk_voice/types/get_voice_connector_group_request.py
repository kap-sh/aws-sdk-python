"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#GetVoiceConnectorGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.non_empty_string


class GetVoiceConnectorGroupRequest(TypedDict):
    voice_connector_group_id: (
        "aws_sdk_chime_sdk_voice.types.non_empty_string.NonEmptyString"
    )
    """<p>The Voice Connector group ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetVoiceConnectorGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetVoiceConnectorGroupRequest:
    out: GetVoiceConnectorGroupRequest = {}  # type: ignore[typeddict-item]
    return out

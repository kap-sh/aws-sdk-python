"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#UpdateVoiceConnectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_chime_sdk_voice.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.boolean
    import aws_sdk_chime_sdk_voice.types.non_empty_string
    import aws_sdk_chime_sdk_voice.types.voice_connector_name


class UpdateVoiceConnectorRequest(TypedDict, closed=True):
    voice_connector_id: "aws_sdk_chime_sdk_voice.types.non_empty_string.NonEmptyString"
    """<p>The Voice Connector ID.</p>"""
    name: "aws_sdk_chime_sdk_voice.types.voice_connector_name.VoiceConnectorName"
    """<p>The name of the Voice Connector.</p>"""
    require_encryption: "aws_sdk_chime_sdk_voice.types.boolean.Boolean"
    """<p>When enabled, requires encryption for the Voice Connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateVoiceConnectorRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["RequireEncryption"] = value["require_encryption"]
    return out


def deserialize_json(data: dict) -> UpdateVoiceConnectorRequest:
    out: UpdateVoiceConnectorRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateVoiceConnectorRequest.name required")
    if "RequireEncryption" in data:
        out["require_encryption"] = data["RequireEncryption"]
    else:
        raise DeserializationError(
            "UpdateVoiceConnectorRequest.require_encryption required"
        )
    return out

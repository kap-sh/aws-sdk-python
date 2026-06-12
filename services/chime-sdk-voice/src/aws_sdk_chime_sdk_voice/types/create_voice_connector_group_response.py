"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#CreateVoiceConnectorGroupResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.voice_connector_group


class CreateVoiceConnectorGroupResponse(TypedDict):
    voice_connector_group: NotRequired[
        "aws_sdk_chime_sdk_voice.types.voice_connector_group.VoiceConnectorGroup"
    ]
    """<p>The details of the Voice Connector group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateVoiceConnectorGroupResponse) -> dict:
    out: dict = {}
    if "voice_connector_group" in value:
        import aws_sdk_chime_sdk_voice.types.voice_connector_group

        out["VoiceConnectorGroup"] = (
            aws_sdk_chime_sdk_voice.types.voice_connector_group.serialize_json(
                value["voice_connector_group"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateVoiceConnectorGroupResponse:
    out: CreateVoiceConnectorGroupResponse = {}  # type: ignore[typeddict-item]
    if "VoiceConnectorGroup" in data:
        import aws_sdk_chime_sdk_voice.types.voice_connector_group

        out["voice_connector_group"] = (
            aws_sdk_chime_sdk_voice.types.voice_connector_group.deserialize_json(
                data["VoiceConnectorGroup"]
            )
        )
    return out

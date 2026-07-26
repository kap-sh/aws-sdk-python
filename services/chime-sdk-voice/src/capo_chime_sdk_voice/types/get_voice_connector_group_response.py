"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#GetVoiceConnectorGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.voice_connector_group


class GetVoiceConnectorGroupResponse(TypedDict, closed=True):
    voice_connector_group: NotRequired[
        "capo_chime_sdk_voice.types.voice_connector_group.VoiceConnectorGroup"
    ]
    """<p>The details of the Voice Connector group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetVoiceConnectorGroupResponse) -> dict:
    out: dict = {}
    if "voice_connector_group" in value:
        import capo_chime_sdk_voice.types.voice_connector_group

        out["VoiceConnectorGroup"] = (
            capo_chime_sdk_voice.types.voice_connector_group.serialize_json(
                value["voice_connector_group"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetVoiceConnectorGroupResponse:
    out: GetVoiceConnectorGroupResponse = {}  # type: ignore[typeddict-item]
    if "VoiceConnectorGroup" in data:
        import capo_chime_sdk_voice.types.voice_connector_group

        out["voice_connector_group"] = (
            capo_chime_sdk_voice.types.voice_connector_group.deserialize_json(
                data["VoiceConnectorGroup"]
            )
        )
    return out

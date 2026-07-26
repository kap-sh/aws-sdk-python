"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#VoiceConnectorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.voice_connector

VoiceConnectorList: TypeAlias = list[
    "capo_chime_sdk_voice.types.voice_connector.VoiceConnector"
]


# --- restJson1 ser/de ---
def serialize_json(value: VoiceConnectorList) -> list:
    import capo_chime_sdk_voice.types.voice_connector

    out: list = []
    for item in value:
        out.append(capo_chime_sdk_voice.types.voice_connector.serialize_json(item))
    return out


def deserialize_json(data: list) -> VoiceConnectorList:
    import capo_chime_sdk_voice.types.voice_connector

    out: VoiceConnectorList = []
    for item in data:
        out.append(capo_chime_sdk_voice.types.voice_connector.deserialize_json(item))
    return out

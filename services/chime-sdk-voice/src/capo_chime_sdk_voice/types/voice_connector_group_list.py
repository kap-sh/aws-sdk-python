"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#VoiceConnectorGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.voice_connector_group

VoiceConnectorGroupList: TypeAlias = list[
    "capo_chime_sdk_voice.types.voice_connector_group.VoiceConnectorGroup"
]


# --- restJson1 ser/de ---
def serialize_json(value: VoiceConnectorGroupList) -> list:
    import capo_chime_sdk_voice.types.voice_connector_group

    out: list = []
    for item in value:
        out.append(
            capo_chime_sdk_voice.types.voice_connector_group.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> VoiceConnectorGroupList:
    import capo_chime_sdk_voice.types.voice_connector_group

    out: VoiceConnectorGroupList = []
    for item in data:
        out.append(
            capo_chime_sdk_voice.types.voice_connector_group.deserialize_json(item)
        )
    return out

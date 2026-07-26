"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#VoiceConnectorItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.voice_connector_item

VoiceConnectorItemList: TypeAlias = list[
    "capo_chime_sdk_voice.types.voice_connector_item.VoiceConnectorItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: VoiceConnectorItemList) -> list:
    import capo_chime_sdk_voice.types.voice_connector_item

    out: list = []
    for item in value:
        out.append(capo_chime_sdk_voice.types.voice_connector_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> VoiceConnectorItemList:
    import capo_chime_sdk_voice.types.voice_connector_item

    out: VoiceConnectorItemList = []
    for item in data:
        out.append(
            capo_chime_sdk_voice.types.voice_connector_item.deserialize_json(item)
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#VoiceConnectorGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.voice_connector_group

VoiceConnectorGroupList: TypeAlias = list[
    "aws_sdk_chime_sdk_voice.types.voice_connector_group.VoiceConnectorGroup"
]


# --- restJson1 ser/de ---
def serialize_json(value: VoiceConnectorGroupList) -> list:
    import aws_sdk_chime_sdk_voice.types.voice_connector_group

    out: list = []
    for item in value:
        out.append(
            aws_sdk_chime_sdk_voice.types.voice_connector_group.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> VoiceConnectorGroupList:
    import aws_sdk_chime_sdk_voice.types.voice_connector_group

    out: VoiceConnectorGroupList = []
    for item in data:
        out.append(
            aws_sdk_chime_sdk_voice.types.voice_connector_group.deserialize_json(item)
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.connect#VoiceEnhancementConfigs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.voice_enhancement_config

VoiceEnhancementConfigs: TypeAlias = list[
    "aws_sdk_connect.types.voice_enhancement_config.VoiceEnhancementConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: VoiceEnhancementConfigs) -> list:
    import aws_sdk_connect.types.voice_enhancement_config

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.voice_enhancement_config.serialize_json(item))
    return out


def deserialize_json(data: list) -> VoiceEnhancementConfigs:
    import aws_sdk_connect.types.voice_enhancement_config

    out: VoiceEnhancementConfigs = []
    for item in data:
        out.append(
            aws_sdk_connect.types.voice_enhancement_config.deserialize_json(item)
        )
    return out

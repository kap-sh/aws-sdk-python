"""Generated from Smithy shape ``com.amazonaws.connect#VoiceEnhancementConfigs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.voice_enhancement_config

VoiceEnhancementConfigs: TypeAlias = list[
    "capo_connect.types.voice_enhancement_config.VoiceEnhancementConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: VoiceEnhancementConfigs) -> list:
    import capo_connect.types.voice_enhancement_config

    out: list = []
    for item in value:
        out.append(capo_connect.types.voice_enhancement_config.serialize_json(item))
    return out


def deserialize_json(data: list) -> VoiceEnhancementConfigs:
    import capo_connect.types.voice_enhancement_config

    out: VoiceEnhancementConfigs = []
    for item in data:
        out.append(capo_connect.types.voice_enhancement_config.deserialize_json(item))
    return out

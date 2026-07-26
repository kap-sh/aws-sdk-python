"""Generated from Smithy shape ``com.amazonaws.ivs#AudioConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ivs.types.audio_configuration

AudioConfigurationList: TypeAlias = list[
    "capo_ivs.types.audio_configuration.AudioConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: AudioConfigurationList) -> list:
    import capo_ivs.types.audio_configuration

    out: list = []
    for item in value:
        out.append(capo_ivs.types.audio_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> AudioConfigurationList:
    import capo_ivs.types.audio_configuration

    out: AudioConfigurationList = []
    for item in data:
        out.append(capo_ivs.types.audio_configuration.deserialize_json(item))
    return out

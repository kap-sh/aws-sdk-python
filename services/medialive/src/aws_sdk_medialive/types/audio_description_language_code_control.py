"""Generated from Smithy shape ``com.amazonaws.medialive#AudioDescriptionLanguageCodeControl``."""

from typing import Literal, TypeAlias, cast

"""Audio Description Language Code Control"""
AudioDescriptionLanguageCodeControl: TypeAlias = Literal[
    "FOLLOW_INPUT",
    "USE_CONFIGURED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AudioDescriptionLanguageCodeControl) -> str:
    return value


def deserialize_json(data: str) -> AudioDescriptionLanguageCodeControl:
    return cast(AudioDescriptionLanguageCodeControl, data)

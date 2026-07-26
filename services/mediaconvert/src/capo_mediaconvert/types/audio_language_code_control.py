"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AudioLanguageCodeControl``."""

from typing import Literal, TypeAlias, cast

"""Specify which source for language code takes precedence for this audio track. When you choose Follow input, the service uses the language code from the input track if it's present. If there's no languge code on the input track, the service uses the code that you specify in the setting Language code. When you choose Use configured, the service uses the language code that you specify."""
AudioLanguageCodeControl: TypeAlias = Literal[
    "FOLLOW_INPUT",
    "USE_CONFIGURED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AudioLanguageCodeControl) -> str:
    return value


def deserialize_json(data: str) -> AudioLanguageCodeControl:
    return cast(AudioLanguageCodeControl, data)

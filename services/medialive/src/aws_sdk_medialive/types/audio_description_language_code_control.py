"""Generated from Smithy shape ``com.amazonaws.medialive#AudioDescriptionLanguageCodeControl``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Audio Description Language Code Control"""
AudioDescriptionLanguageCodeControl: TypeAlias = Literal[
    "FOLLOW_INPUT",
    "USE_CONFIGURED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FOLLOW_INPUT",
        "USE_CONFIGURED",
    )
)


def serialize_json(value: AudioDescriptionLanguageCodeControl) -> str:
    return value


def deserialize_json(data: str) -> AudioDescriptionLanguageCodeControl:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AudioDescriptionLanguageCodeControl value: {data!r}"
        )
    return cast(AudioDescriptionLanguageCodeControl, data)

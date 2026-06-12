"""Generated from Smithy shape ``com.amazonaws.medialive#AudioLanguageSelectionPolicy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Audio Language Selection Policy"""
AudioLanguageSelectionPolicy: TypeAlias = Literal[
    "LOOSE",
    "STRICT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LOOSE",
        "STRICT",
    )
)


def serialize_json(value: AudioLanguageSelectionPolicy) -> str:
    return value


def deserialize_json(data: str) -> AudioLanguageSelectionPolicy:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AudioLanguageSelectionPolicy value: {data!r}"
        )
    return cast(AudioLanguageSelectionPolicy, data)

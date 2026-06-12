"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#Pronouns``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transcribe_streaming.errors import DeserializationError

Pronouns: TypeAlias = Literal[
    "HE_HIM",
    "SHE_HER",
    "THEY_THEM",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HE_HIM",
        "SHE_HER",
        "THEY_THEM",
    )
)


def serialize_json(value: Pronouns) -> str:
    return value


def deserialize_json(data: str) -> Pronouns:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Pronouns value: {data!r}")
    return cast(Pronouns, data)

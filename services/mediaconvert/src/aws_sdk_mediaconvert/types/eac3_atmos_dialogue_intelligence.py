"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Eac3AtmosDialogueIntelligence``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Enable Dolby Dialogue Intelligence to adjust loudness based on dialogue analysis."""
Eac3AtmosDialogueIntelligence: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: Eac3AtmosDialogueIntelligence) -> str:
    return value


def deserialize_json(data: str) -> Eac3AtmosDialogueIntelligence:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown Eac3AtmosDialogueIntelligence value: {data!r}"
        )
    return cast(Eac3AtmosDialogueIntelligence, data)

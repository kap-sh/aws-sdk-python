"""Generated from Smithy shape ``com.amazonaws.medialive#NielsenPcmToId3TaggingState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""State of Nielsen PCM to ID3 tagging"""
NielsenPcmToId3TaggingState: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "ENABLED",
    )
)


def serialize_json(value: NielsenPcmToId3TaggingState) -> str:
    return value


def deserialize_json(data: str) -> NielsenPcmToId3TaggingState:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown NielsenPcmToId3TaggingState value: {data!r}"
        )
    return cast(NielsenPcmToId3TaggingState, data)

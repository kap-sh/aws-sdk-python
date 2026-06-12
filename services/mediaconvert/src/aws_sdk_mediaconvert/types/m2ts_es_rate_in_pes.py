"""Generated from Smithy shape ``com.amazonaws.mediaconvert#M2tsEsRateInPes``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Controls whether to include the ES Rate field in the PES header."""
M2tsEsRateInPes: TypeAlias = Literal[
    "INCLUDE",
    "EXCLUDE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INCLUDE",
        "EXCLUDE",
    )
)


def serialize_json(value: M2tsEsRateInPes) -> str:
    return value


def deserialize_json(data: str) -> M2tsEsRateInPes:
    if data not in _VALUES:
        raise DeserializationError(f"unknown M2tsEsRateInPes value: {data!r}")
    return cast(M2tsEsRateInPes, data)

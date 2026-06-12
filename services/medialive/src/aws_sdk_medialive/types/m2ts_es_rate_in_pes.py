"""Generated from Smithy shape ``com.amazonaws.medialive#M2tsEsRateInPes``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""M2ts Es Rate In Pes"""
M2tsEsRateInPes: TypeAlias = Literal[
    "EXCLUDE",
    "INCLUDE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EXCLUDE",
        "INCLUDE",
    )
)


def serialize_json(value: M2tsEsRateInPes) -> str:
    return value


def deserialize_json(data: str) -> M2tsEsRateInPes:
    if data not in _VALUES:
        raise DeserializationError(f"unknown M2tsEsRateInPes value: {data!r}")
    return cast(M2tsEsRateInPes, data)

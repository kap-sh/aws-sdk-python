"""Generated from Smithy shape ``com.amazonaws.outposts#PowerPhase``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_outposts.errors import DeserializationError

PowerPhase: TypeAlias = Literal[
    "SINGLE_PHASE",
    "THREE_PHASE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SINGLE_PHASE",
        "THREE_PHASE",
    )
)


def serialize_json(value: PowerPhase) -> str:
    return value


def deserialize_json(data: str) -> PowerPhase:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PowerPhase value: {data!r}")
    return cast(PowerPhase, data)

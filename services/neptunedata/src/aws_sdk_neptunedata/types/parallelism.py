"""Generated from Smithy shape ``com.amazonaws.neptunedata#Parallelism``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_neptunedata.errors import DeserializationError

Parallelism: TypeAlias = Literal[
    "LOW",
    "MEDIUM",
    "HIGH",
    "OVERSUBSCRIBE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LOW",
        "MEDIUM",
        "HIGH",
        "OVERSUBSCRIBE",
    )
)


def serialize_json(value: Parallelism) -> str:
    return value


def deserialize_json(data: str) -> Parallelism:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Parallelism value: {data!r}")
    return cast(Parallelism, data)

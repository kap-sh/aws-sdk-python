"""Generated from Smithy shape ``com.amazonaws.auditmanager#SourceFrequency``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auditmanager.errors import DeserializationError

SourceFrequency: TypeAlias = Literal[
    "DAILY",
    "WEEKLY",
    "MONTHLY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DAILY",
        "WEEKLY",
        "MONTHLY",
    )
)


def serialize_json(value: SourceFrequency) -> str:
    return value


def deserialize_json(data: str) -> SourceFrequency:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SourceFrequency value: {data!r}")
    return cast(SourceFrequency, data)

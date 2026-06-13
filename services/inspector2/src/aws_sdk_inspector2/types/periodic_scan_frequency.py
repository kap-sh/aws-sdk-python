"""Generated from Smithy shape ``com.amazonaws.inspector2#PeriodicScanFrequency``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_inspector2.errors import DeserializationError

PeriodicScanFrequency: TypeAlias = Literal[
    "WEEKLY",
    "MONTHLY",
    "NEVER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "WEEKLY",
        "MONTHLY",
        "NEVER",
    )
)


def serialize_json(value: PeriodicScanFrequency) -> str:
    return value


def deserialize_json(data: str) -> PeriodicScanFrequency:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PeriodicScanFrequency value: {data!r}")
    return cast(PeriodicScanFrequency, data)

"""Generated from Smithy shape ``com.amazonaws.applicationsignals#DurationUnit``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_application_signals.errors import DeserializationError

DurationUnit: TypeAlias = Literal[
    "MINUTE",
    "HOUR",
    "DAY",
    "MONTH",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MINUTE",
        "HOUR",
        "DAY",
        "MONTH",
    )
)


def serialize_json(value: DurationUnit) -> str:
    return value


def deserialize_json(data: str) -> DurationUnit:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DurationUnit value: {data!r}")
    return cast(DurationUnit, data)

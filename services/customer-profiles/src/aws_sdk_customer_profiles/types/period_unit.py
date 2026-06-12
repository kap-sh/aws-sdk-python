"""Generated from Smithy shape ``com.amazonaws.customerprofiles#PeriodUnit``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_customer_profiles.errors import DeserializationError

PeriodUnit: TypeAlias = Literal[
    "MINUTES",
    "HOURS",
    "DAYS",
    "WEEKS",
    "MONTHS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MINUTES",
        "HOURS",
        "DAYS",
        "WEEKS",
        "MONTHS",
    )
)


def serialize_json(value: PeriodUnit) -> str:
    return value


def deserialize_json(data: str) -> PeriodUnit:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PeriodUnit value: {data!r}")
    return cast(PeriodUnit, data)

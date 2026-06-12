"""Generated from Smithy shape ``com.amazonaws.customerprofiles#Statistic``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_customer_profiles.errors import DeserializationError

Statistic: TypeAlias = Literal[
    "FIRST_OCCURRENCE",
    "LAST_OCCURRENCE",
    "COUNT",
    "SUM",
    "MINIMUM",
    "MAXIMUM",
    "AVERAGE",
    "MAX_OCCURRENCE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FIRST_OCCURRENCE",
        "LAST_OCCURRENCE",
        "COUNT",
        "SUM",
        "MINIMUM",
        "MAXIMUM",
        "AVERAGE",
        "MAX_OCCURRENCE",
    )
)


def serialize_json(value: Statistic) -> str:
    return value


def deserialize_json(data: str) -> Statistic:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Statistic value: {data!r}")
    return cast(Statistic, data)

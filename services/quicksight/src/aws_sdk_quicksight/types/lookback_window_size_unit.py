"""Generated from Smithy shape ``com.amazonaws.quicksight#LookbackWindowSizeUnit``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

LookbackWindowSizeUnit: TypeAlias = Literal[
    "HOUR",
    "DAY",
    "WEEK",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HOUR",
        "DAY",
        "WEEK",
    )
)


def serialize_json(value: LookbackWindowSizeUnit) -> str:
    return value


def deserialize_json(data: str) -> LookbackWindowSizeUnit:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LookbackWindowSizeUnit value: {data!r}")
    return cast(LookbackWindowSizeUnit, data)

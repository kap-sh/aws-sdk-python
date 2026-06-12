"""Generated from Smithy shape ``com.amazonaws.dlm#RetentionIntervalUnitValues``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_dlm.errors import DeserializationError

RetentionIntervalUnitValues: TypeAlias = Literal[
    "DAYS",
    "WEEKS",
    "MONTHS",
    "YEARS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DAYS",
        "WEEKS",
        "MONTHS",
        "YEARS",
    )
)


def serialize_json(value: RetentionIntervalUnitValues) -> str:
    return value


def deserialize_json(data: str) -> RetentionIntervalUnitValues:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RetentionIntervalUnitValues value: {data!r}"
        )
    return cast(RetentionIntervalUnitValues, data)

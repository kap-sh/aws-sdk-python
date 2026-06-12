"""Generated from Smithy shape ``com.amazonaws.pinpoint#Duration``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pinpoint.errors import DeserializationError

Duration: TypeAlias = Literal[
    "HR_24",
    "DAY_7",
    "DAY_14",
    "DAY_30",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HR_24",
        "DAY_7",
        "DAY_14",
        "DAY_30",
    )
)


def serialize_json(value: Duration) -> str:
    return value


def deserialize_json(data: str) -> Duration:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Duration value: {data!r}")
    return cast(Duration, data)

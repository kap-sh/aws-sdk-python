"""Generated from Smithy shape ``com.amazonaws.iot#DayOfWeek``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

DayOfWeek: TypeAlias = Literal[
    "SUN",
    "MON",
    "TUE",
    "WED",
    "THU",
    "FRI",
    "SAT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUN",
        "MON",
        "TUE",
        "WED",
        "THU",
        "FRI",
        "SAT",
    )
)


def serialize_json(value: DayOfWeek) -> str:
    return value


def deserialize_json(data: str) -> DayOfWeek:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DayOfWeek value: {data!r}")
    return cast(DayOfWeek, data)

"""Generated from Smithy shape ``com.amazonaws.inspector2#Day``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_inspector2.errors import DeserializationError

Day: TypeAlias = Literal[
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


def serialize_json(value: Day) -> str:
    return value


def deserialize_json(data: str) -> Day:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Day value: {data!r}")
    return cast(Day, data)

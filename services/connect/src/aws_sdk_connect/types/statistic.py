"""Generated from Smithy shape ``com.amazonaws.connect#Statistic``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

Statistic: TypeAlias = Literal[
    "SUM",
    "MAX",
    "AVG",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUM",
        "MAX",
        "AVG",
    )
)


def serialize_json(value: Statistic) -> str:
    return value


def deserialize_json(data: str) -> Statistic:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Statistic value: {data!r}")
    return cast(Statistic, data)

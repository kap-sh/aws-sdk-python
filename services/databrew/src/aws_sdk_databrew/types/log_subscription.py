"""Generated from Smithy shape ``com.amazonaws.databrew#LogSubscription``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_databrew.errors import DeserializationError

LogSubscription: TypeAlias = Literal[
    "ENABLE",
    "DISABLE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLE",
        "DISABLE",
    )
)


def serialize_json(value: LogSubscription) -> str:
    return value


def deserialize_json(data: str) -> LogSubscription:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LogSubscription value: {data!r}")
    return cast(LogSubscription, data)

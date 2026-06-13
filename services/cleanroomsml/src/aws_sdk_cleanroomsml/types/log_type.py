"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#LogType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanroomsml.errors import DeserializationError

LogType: TypeAlias = Literal[
    "ALL",
    "ERROR_SUMMARY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL",
        "ERROR_SUMMARY",
    )
)


def serialize_json(value: LogType) -> str:
    return value


def deserialize_json(data: str) -> LogType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LogType value: {data!r}")
    return cast(LogType, data)

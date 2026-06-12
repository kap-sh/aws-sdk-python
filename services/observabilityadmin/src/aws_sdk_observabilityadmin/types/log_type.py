"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#LogType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_observabilityadmin.errors import DeserializationError

LogType: TypeAlias = Literal[
    "APPLICATION_LOGS",
    "USAGE_LOGS",
    "SECURITY_FINDING_LOGS",
    "ACCESS_LOGS",
    "CONNECTION_LOGS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "APPLICATION_LOGS",
        "USAGE_LOGS",
        "SECURITY_FINDING_LOGS",
        "ACCESS_LOGS",
        "CONNECTION_LOGS",
    )
)


def serialize_json(value: LogType) -> str:
    return value


def deserialize_json(data: str) -> LogType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LogType value: {data!r}")
    return cast(LogType, data)

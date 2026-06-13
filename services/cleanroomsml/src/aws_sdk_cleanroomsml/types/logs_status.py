"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#LogsStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanroomsml.errors import DeserializationError

LogsStatus: TypeAlias = Literal[
    "PUBLISH_SUCCEEDED",
    "PUBLISH_FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PUBLISH_SUCCEEDED",
        "PUBLISH_FAILED",
    )
)


def serialize_json(value: LogsStatus) -> str:
    return value


def deserialize_json(data: str) -> LogsStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LogsStatus value: {data!r}")
    return cast(LogsStatus, data)

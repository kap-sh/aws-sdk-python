"""Generated from Smithy shape ``com.amazonaws.iotsitewise#MonitorErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotsitewise.errors import DeserializationError

MonitorErrorCode: TypeAlias = Literal[
    "INTERNAL_FAILURE",
    "VALIDATION_ERROR",
    "LIMIT_EXCEEDED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INTERNAL_FAILURE",
        "VALIDATION_ERROR",
        "LIMIT_EXCEEDED",
    )
)


def serialize_json(value: MonitorErrorCode) -> str:
    return value


def deserialize_json(data: str) -> MonitorErrorCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MonitorErrorCode value: {data!r}")
    return cast(MonitorErrorCode, data)

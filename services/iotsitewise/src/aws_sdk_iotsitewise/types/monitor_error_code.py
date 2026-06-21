"""Generated from Smithy shape ``com.amazonaws.iotsitewise#MonitorErrorCode``."""

from typing import Literal, TypeAlias, cast

MonitorErrorCode: TypeAlias = Literal[
    "INTERNAL_FAILURE",
    "VALIDATION_ERROR",
    "LIMIT_EXCEEDED",
]


# --- restJson1 ser/de ---
def serialize_json(value: MonitorErrorCode) -> str:
    return value


def deserialize_json(data: str) -> MonitorErrorCode:
    return cast(MonitorErrorCode, data)

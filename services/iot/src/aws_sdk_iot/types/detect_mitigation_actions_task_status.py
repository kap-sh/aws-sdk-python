"""Generated from Smithy shape ``com.amazonaws.iot#DetectMitigationActionsTaskStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

DetectMitigationActionsTaskStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "SUCCESSFUL",
    "FAILED",
    "CANCELED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "SUCCESSFUL",
        "FAILED",
        "CANCELED",
    )
)


def serialize_json(value: DetectMitigationActionsTaskStatus) -> str:
    return value


def deserialize_json(data: str) -> DetectMitigationActionsTaskStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DetectMitigationActionsTaskStatus value: {data!r}"
        )
    return cast(DetectMitigationActionsTaskStatus, data)

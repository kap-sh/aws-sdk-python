"""Generated from Smithy shape ``com.amazonaws.iot#DetectMitigationActionExecutionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

DetectMitigationActionExecutionStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "SUCCESSFUL",
    "FAILED",
    "SKIPPED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "SUCCESSFUL",
        "FAILED",
        "SKIPPED",
    )
)


def serialize_json(value: DetectMitigationActionExecutionStatus) -> str:
    return value


def deserialize_json(data: str) -> DetectMitigationActionExecutionStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DetectMitigationActionExecutionStatus value: {data!r}"
        )
    return cast(DetectMitigationActionExecutionStatus, data)

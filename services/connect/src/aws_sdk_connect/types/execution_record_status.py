"""Generated from Smithy shape ``com.amazonaws.connect#ExecutionRecordStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

ExecutionRecordStatus: TypeAlias = Literal[
    "PASSED",
    "FAILED",
    "IN_PROGRESS",
    "STOPPED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PASSED",
        "FAILED",
        "IN_PROGRESS",
        "STOPPED",
    )
)


def serialize_json(value: ExecutionRecordStatus) -> str:
    return value


def deserialize_json(data: str) -> ExecutionRecordStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExecutionRecordStatus value: {data!r}")
    return cast(ExecutionRecordStatus, data)

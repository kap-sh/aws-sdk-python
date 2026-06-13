"""Generated from Smithy shape ``com.amazonaws.securityir#ExecutionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_security_ir.errors import DeserializationError

ExecutionStatus: TypeAlias = Literal[
    "Pending",
    "InProgress",
    "Waiting",
    "Completed",
    "Failed",
    "Cancelled",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Pending",
        "InProgress",
        "Waiting",
        "Completed",
        "Failed",
        "Cancelled",
    )
)


def serialize_json(value: ExecutionStatus) -> str:
    return value


def deserialize_json(data: str) -> ExecutionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExecutionStatus value: {data!r}")
    return cast(ExecutionStatus, data)

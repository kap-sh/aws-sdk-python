"""Generated from Smithy shape ``com.amazonaws.qapps#ExecutionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qapps.errors import DeserializationError

ExecutionStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "WAITING",
    "COMPLETED",
    "ERROR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "WAITING",
        "COMPLETED",
        "ERROR",
    )
)


def serialize_json(value: ExecutionStatus) -> str:
    return value


def deserialize_json(data: str) -> ExecutionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExecutionStatus value: {data!r}")
    return cast(ExecutionStatus, data)

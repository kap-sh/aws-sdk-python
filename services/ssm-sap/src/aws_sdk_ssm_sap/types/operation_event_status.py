"""Generated from Smithy shape ``com.amazonaws.ssmsap#OperationEventStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm_sap.errors import DeserializationError

OperationEventStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "COMPLETED",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "COMPLETED",
        "FAILED",
    )
)


def serialize_json(value: OperationEventStatus) -> str:
    return value


def deserialize_json(data: str) -> OperationEventStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OperationEventStatus value: {data!r}")
    return cast(OperationEventStatus, data)

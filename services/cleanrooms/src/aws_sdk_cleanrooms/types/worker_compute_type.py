"""Generated from Smithy shape ``com.amazonaws.cleanrooms#WorkerComputeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanrooms.errors import DeserializationError

WorkerComputeType: TypeAlias = Literal[
    "CR.1X",
    "CR.4X",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CR.1X",
        "CR.4X",
    )
)


def serialize_json(value: WorkerComputeType) -> str:
    return value


def deserialize_json(data: str) -> WorkerComputeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WorkerComputeType value: {data!r}")
    return cast(WorkerComputeType, data)

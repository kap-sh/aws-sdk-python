"""Generated from Smithy shape ``com.amazonaws.controltower#BaselineOperationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_controltower.errors import DeserializationError

BaselineOperationStatus: TypeAlias = Literal[
    "SUCCEEDED",
    "FAILED",
    "IN_PROGRESS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUCCEEDED",
        "FAILED",
        "IN_PROGRESS",
    )
)


def serialize_json(value: BaselineOperationStatus) -> str:
    return value


def deserialize_json(data: str) -> BaselineOperationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BaselineOperationStatus value: {data!r}")
    return cast(BaselineOperationStatus, data)

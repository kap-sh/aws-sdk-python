"""Generated from Smithy shape ``com.amazonaws.eks#UpdateStatus``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_eks.errors import DeserializationError

UpdateStatus: TypeAlias = Literal[
    "InProgress",
    "Failed",
    "Cancelled",
    "Successful",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InProgress",
        "Failed",
        "Cancelled",
        "Successful",
    )
)


def serialize_json(value: UpdateStatus) -> str:
    return value


def deserialize_json(data: str) -> UpdateStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UpdateStatus value: {data!r}")
    return cast(UpdateStatus, data)

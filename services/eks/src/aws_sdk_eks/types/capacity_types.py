"""Generated from Smithy shape ``com.amazonaws.eks#CapacityTypes``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_eks.errors import DeserializationError

CapacityTypes: TypeAlias = Literal[
    "ON_DEMAND",
    "SPOT",
    "CAPACITY_BLOCK",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ON_DEMAND",
        "SPOT",
        "CAPACITY_BLOCK",
    )
)


def serialize_json(value: CapacityTypes) -> str:
    return value


def deserialize_json(data: str) -> CapacityTypes:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CapacityTypes value: {data!r}")
    return cast(CapacityTypes, data)

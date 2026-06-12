"""Generated from Smithy shape ``com.amazonaws.devopsguru#CostEstimationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_devops_guru.errors import DeserializationError

CostEstimationStatus: TypeAlias = Literal[
    "ONGOING",
    "COMPLETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ONGOING",
        "COMPLETED",
    )
)


def serialize_json(value: CostEstimationStatus) -> str:
    return value


def deserialize_json(data: str) -> CostEstimationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CostEstimationStatus value: {data!r}")
    return cast(CostEstimationStatus, data)

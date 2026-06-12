"""Generated from Smithy shape ``com.amazonaws.devopsguru#CostEstimationServiceResourceState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_devops_guru.errors import DeserializationError

CostEstimationServiceResourceState: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "INACTIVE",
    )
)


def serialize_json(value: CostEstimationServiceResourceState) -> str:
    return value


def deserialize_json(data: str) -> CostEstimationServiceResourceState:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CostEstimationServiceResourceState value: {data!r}"
        )
    return cast(CostEstimationServiceResourceState, data)

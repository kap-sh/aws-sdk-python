"""Generated from Smithy shape ``com.amazonaws.resiliencehub#EstimatedCostTier``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehub.errors import DeserializationError

EstimatedCostTier: TypeAlias = Literal[
    "L1",
    "L2",
    "L3",
    "L4",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "L1",
        "L2",
        "L3",
        "L4",
    )
)


def serialize_json(value: EstimatedCostTier) -> str:
    return value


def deserialize_json(data: str) -> EstimatedCostTier:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EstimatedCostTier value: {data!r}")
    return cast(EstimatedCostTier, data)

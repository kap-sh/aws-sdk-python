"""Generated from Smithy shape ``com.amazonaws.lambda#SnapStartOptimizationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lambda.errors import DeserializationError

SnapStartOptimizationStatus: TypeAlias = Literal[
    "On",
    "Off",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "On",
        "Off",
    )
)


def serialize_json(value: SnapStartOptimizationStatus) -> str:
    return value


def deserialize_json(data: str) -> SnapStartOptimizationStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SnapStartOptimizationStatus value: {data!r}"
        )
    return cast(SnapStartOptimizationStatus, data)

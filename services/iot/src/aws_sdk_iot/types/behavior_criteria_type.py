"""Generated from Smithy shape ``com.amazonaws.iot#BehaviorCriteriaType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

BehaviorCriteriaType: TypeAlias = Literal[
    "STATIC",
    "STATISTICAL",
    "MACHINE_LEARNING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STATIC",
        "STATISTICAL",
        "MACHINE_LEARNING",
    )
)


def serialize_json(value: BehaviorCriteriaType) -> str:
    return value


def deserialize_json(data: str) -> BehaviorCriteriaType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BehaviorCriteriaType value: {data!r}")
    return cast(BehaviorCriteriaType, data)

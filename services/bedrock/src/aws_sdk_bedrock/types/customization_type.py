"""Generated from Smithy shape ``com.amazonaws.bedrock#CustomizationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

CustomizationType: TypeAlias = Literal[
    "FINE_TUNING",
    "CONTINUED_PRE_TRAINING",
    "DISTILLATION",
    "REINFORCEMENT_FINE_TUNING",
    "IMPORTED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FINE_TUNING",
        "CONTINUED_PRE_TRAINING",
        "DISTILLATION",
        "REINFORCEMENT_FINE_TUNING",
        "IMPORTED",
    )
)


def serialize_json(value: CustomizationType) -> str:
    return value


def deserialize_json(data: str) -> CustomizationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CustomizationType value: {data!r}")
    return cast(CustomizationType, data)

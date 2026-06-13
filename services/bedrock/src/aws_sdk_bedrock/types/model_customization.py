"""Generated from Smithy shape ``com.amazonaws.bedrock#ModelCustomization``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

ModelCustomization: TypeAlias = Literal[
    "FINE_TUNING",
    "CONTINUED_PRE_TRAINING",
    "DISTILLATION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FINE_TUNING",
        "CONTINUED_PRE_TRAINING",
        "DISTILLATION",
    )
)


def serialize_json(value: ModelCustomization) -> str:
    return value


def deserialize_json(data: str) -> ModelCustomization:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ModelCustomization value: {data!r}")
    return cast(ModelCustomization, data)

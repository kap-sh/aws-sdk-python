"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SlotResolutionStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

SlotResolutionStrategy: TypeAlias = Literal[
    "EnhancedFallback",
    "Default",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EnhancedFallback",
        "Default",
    )
)


def serialize_json(value: SlotResolutionStrategy) -> str:
    return value


def deserialize_json(data: str) -> SlotResolutionStrategy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SlotResolutionStrategy value: {data!r}")
    return cast(SlotResolutionStrategy, data)

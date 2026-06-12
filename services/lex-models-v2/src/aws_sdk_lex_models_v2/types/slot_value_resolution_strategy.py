"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SlotValueResolutionStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

SlotValueResolutionStrategy: TypeAlias = Literal[
    "OriginalValue",
    "TopResolution",
    "Concatenation",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OriginalValue",
        "TopResolution",
        "Concatenation",
    )
)


def serialize_json(value: SlotValueResolutionStrategy) -> str:
    return value


def deserialize_json(data: str) -> SlotValueResolutionStrategy:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SlotValueResolutionStrategy value: {data!r}"
        )
    return cast(SlotValueResolutionStrategy, data)

"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#SlotValueSelectionStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_model_building_service.errors import DeserializationError

SlotValueSelectionStrategy: TypeAlias = Literal[
    "ORIGINAL_VALUE",
    "TOP_RESOLUTION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ORIGINAL_VALUE",
        "TOP_RESOLUTION",
    )
)


def serialize_json(value: SlotValueSelectionStrategy) -> str:
    return value


def deserialize_json(data: str) -> SlotValueSelectionStrategy:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SlotValueSelectionStrategy value: {data!r}"
        )
    return cast(SlotValueSelectionStrategy, data)

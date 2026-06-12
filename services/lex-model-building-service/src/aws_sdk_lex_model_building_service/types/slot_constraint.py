"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#SlotConstraint``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_model_building_service.errors import DeserializationError

SlotConstraint: TypeAlias = Literal[
    "Required",
    "Optional",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Required",
        "Optional",
    )
)


def serialize_json(value: SlotConstraint) -> str:
    return value


def deserialize_json(data: str) -> SlotConstraint:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SlotConstraint value: {data!r}")
    return cast(SlotConstraint, data)

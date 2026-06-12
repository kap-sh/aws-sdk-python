"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SlotTypeFilterOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

SlotTypeFilterOperator: TypeAlias = Literal[
    "CO",
    "EQ",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CO",
        "EQ",
    )
)


def serialize_json(value: SlotTypeFilterOperator) -> str:
    return value


def deserialize_json(data: str) -> SlotTypeFilterOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SlotTypeFilterOperator value: {data!r}")
    return cast(SlotTypeFilterOperator, data)

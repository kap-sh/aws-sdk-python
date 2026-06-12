"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SlotFilterOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

SlotFilterOperator: TypeAlias = Literal[
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


def serialize_json(value: SlotFilterOperator) -> str:
    return value


def deserialize_json(data: str) -> SlotFilterOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SlotFilterOperator value: {data!r}")
    return cast(SlotFilterOperator, data)

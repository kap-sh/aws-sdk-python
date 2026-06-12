"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SlotShape``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

SlotShape: TypeAlias = Literal[
    "Scalar",
    "List",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Scalar",
        "List",
    )
)


def serialize_json(value: SlotShape) -> str:
    return value


def deserialize_json(data: str) -> SlotShape:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SlotShape value: {data!r}")
    return cast(SlotShape, data)

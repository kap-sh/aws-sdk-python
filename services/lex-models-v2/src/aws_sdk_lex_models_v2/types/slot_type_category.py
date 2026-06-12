"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SlotTypeCategory``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

SlotTypeCategory: TypeAlias = Literal[
    "Custom",
    "Extended",
    "ExternalGrammar",
    "Composite",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Custom",
        "Extended",
        "ExternalGrammar",
        "Composite",
    )
)


def serialize_json(value: SlotTypeCategory) -> str:
    return value


def deserialize_json(data: str) -> SlotTypeCategory:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SlotTypeCategory value: {data!r}")
    return cast(SlotTypeCategory, data)

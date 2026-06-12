"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#StyleType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_runtime_v2.errors import DeserializationError

StyleType: TypeAlias = Literal[
    "Default",
    "SpellByLetter",
    "SpellByWord",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Default",
        "SpellByLetter",
        "SpellByWord",
    )
)


def serialize_json(value: StyleType) -> str:
    return value


def deserialize_json(data: str) -> StyleType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StyleType value: {data!r}")
    return cast(StyleType, data)

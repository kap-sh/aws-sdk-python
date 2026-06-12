"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SearchOrder``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

SearchOrder: TypeAlias = Literal[
    "Ascending",
    "Descending",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Ascending",
        "Descending",
    )
)


def serialize_json(value: SearchOrder) -> str:
    return value


def deserialize_json(data: str) -> SearchOrder:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SearchOrder value: {data!r}")
    return cast(SearchOrder, data)

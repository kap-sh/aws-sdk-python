"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#GenerationSortByAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

GenerationSortByAttribute: TypeAlias = Literal[
    "creationStartTime",
    "lastUpdatedTime",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "creationStartTime",
        "lastUpdatedTime",
    )
)


def serialize_json(value: GenerationSortByAttribute) -> str:
    return value


def deserialize_json(data: str) -> GenerationSortByAttribute:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GenerationSortByAttribute value: {data!r}")
    return cast(GenerationSortByAttribute, data)

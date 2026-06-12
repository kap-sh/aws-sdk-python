"""Generated from Smithy shape ``com.amazonaws.greengrassv2#RecipeOutputFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_greengrassv2.errors import DeserializationError

RecipeOutputFormat: TypeAlias = Literal[
    "JSON",
    "YAML",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "JSON",
        "YAML",
    )
)


def serialize_json(value: RecipeOutputFormat) -> str:
    return value


def deserialize_json(data: str) -> RecipeOutputFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RecipeOutputFormat value: {data!r}")
    return cast(RecipeOutputFormat, data)

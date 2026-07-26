"""Generated from Smithy shape ``com.amazonaws.greengrassv2#RecipeOutputFormat``."""

from typing import Literal, TypeAlias, cast

RecipeOutputFormat: TypeAlias = Literal[
    "JSON",
    "YAML",
]


# --- restJson1 ser/de ---
def serialize_json(value: RecipeOutputFormat) -> str:
    return value


def deserialize_json(data: str) -> RecipeOutputFormat:
    return cast(RecipeOutputFormat, data)

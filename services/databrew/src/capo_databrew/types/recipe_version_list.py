"""Generated from Smithy shape ``com.amazonaws.databrew#RecipeVersionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_databrew.types.recipe_version

RecipeVersionList: TypeAlias = list["capo_databrew.types.recipe_version.RecipeVersion"]


# --- restJson1 ser/de ---
def serialize_json(value: RecipeVersionList) -> list:
    return list(value)


def deserialize_json(data: list) -> RecipeVersionList:
    return list(data)

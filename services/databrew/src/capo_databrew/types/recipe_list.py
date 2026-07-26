"""Generated from Smithy shape ``com.amazonaws.databrew#RecipeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_databrew.types.recipe

RecipeList: TypeAlias = list["capo_databrew.types.recipe.Recipe"]


# --- restJson1 ser/de ---
def serialize_json(value: RecipeList) -> list:
    import capo_databrew.types.recipe

    out: list = []
    for item in value:
        out.append(capo_databrew.types.recipe.serialize_json(item))
    return out


def deserialize_json(data: list) -> RecipeList:
    import capo_databrew.types.recipe

    out: RecipeList = []
    for item in data:
        out.append(capo_databrew.types.recipe.deserialize_json(item))
    return out

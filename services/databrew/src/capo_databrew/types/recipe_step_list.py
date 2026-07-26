"""Generated from Smithy shape ``com.amazonaws.databrew#RecipeStepList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_databrew.types.recipe_step

RecipeStepList: TypeAlias = list["capo_databrew.types.recipe_step.RecipeStep"]


# --- restJson1 ser/de ---
def serialize_json(value: RecipeStepList) -> list:
    import capo_databrew.types.recipe_step

    out: list = []
    for item in value:
        out.append(capo_databrew.types.recipe_step.serialize_json(item))
    return out


def deserialize_json(data: list) -> RecipeStepList:
    import capo_databrew.types.recipe_step

    out: RecipeStepList = []
    for item in data:
        out.append(capo_databrew.types.recipe_step.deserialize_json(item))
    return out

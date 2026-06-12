"""Generated from Smithy shape ``com.amazonaws.databrew#RecipeStepList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_databrew.types.recipe_step

RecipeStepList: TypeAlias = list["aws_sdk_databrew.types.recipe_step.RecipeStep"]


# --- restJson1 ser/de ---
def serialize_json(value: RecipeStepList) -> list:
    import aws_sdk_databrew.types.recipe_step

    out: list = []
    for item in value:
        out.append(aws_sdk_databrew.types.recipe_step.serialize_json(item))
    return out


def deserialize_json(data: list) -> RecipeStepList:
    import aws_sdk_databrew.types.recipe_step

    out: RecipeStepList = []
    for item in data:
        out.append(aws_sdk_databrew.types.recipe_step.deserialize_json(item))
    return out

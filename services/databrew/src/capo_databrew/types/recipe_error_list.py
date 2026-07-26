"""Generated from Smithy shape ``com.amazonaws.databrew#RecipeErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_databrew.types.recipe_version_error_detail

RecipeErrorList: TypeAlias = list[
    "capo_databrew.types.recipe_version_error_detail.RecipeVersionErrorDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecipeErrorList) -> list:
    import capo_databrew.types.recipe_version_error_detail

    out: list = []
    for item in value:
        out.append(capo_databrew.types.recipe_version_error_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> RecipeErrorList:
    import capo_databrew.types.recipe_version_error_detail

    out: RecipeErrorList = []
    for item in data:
        out.append(
            capo_databrew.types.recipe_version_error_detail.deserialize_json(item)
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.databrew#RecipeErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_databrew.types.recipe_version_error_detail

RecipeErrorList: TypeAlias = list[
    "aws_sdk_databrew.types.recipe_version_error_detail.RecipeVersionErrorDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecipeErrorList) -> list:
    import aws_sdk_databrew.types.recipe_version_error_detail

    out: list = []
    for item in value:
        out.append(
            aws_sdk_databrew.types.recipe_version_error_detail.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RecipeErrorList:
    import aws_sdk_databrew.types.recipe_version_error_detail

    out: RecipeErrorList = []
    for item in data:
        out.append(
            aws_sdk_databrew.types.recipe_version_error_detail.deserialize_json(item)
        )
    return out

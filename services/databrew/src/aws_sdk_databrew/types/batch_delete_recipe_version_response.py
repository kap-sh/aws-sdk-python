"""Generated from Smithy shape ``com.amazonaws.databrew#BatchDeleteRecipeVersionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_databrew.types.recipe_error_list
    import aws_sdk_databrew.types.recipe_name


class BatchDeleteRecipeVersionResponse(TypedDict):
    name: "aws_sdk_databrew.types.recipe_name.RecipeName"
    """<p>The name of the recipe that was modified.</p>"""
    errors: NotRequired["aws_sdk_databrew.types.recipe_error_list.RecipeErrorList"]
    """<p>Errors, if any, that occurred while attempting to delete the recipe versions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteRecipeVersionResponse) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "errors" in value:
        import aws_sdk_databrew.types.recipe_error_list

        out["Errors"] = aws_sdk_databrew.types.recipe_error_list.serialize_json(
            value["errors"]
        )
    return out


def deserialize_json(data: dict) -> BatchDeleteRecipeVersionResponse:
    out: BatchDeleteRecipeVersionResponse = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("BatchDeleteRecipeVersionResponse.name required")
    if "Errors" in data:
        import aws_sdk_databrew.types.recipe_error_list

        out["errors"] = aws_sdk_databrew.types.recipe_error_list.deserialize_json(
            data["Errors"]
        )
    return out

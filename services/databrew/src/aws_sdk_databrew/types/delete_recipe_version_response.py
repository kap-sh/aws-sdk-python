"""Generated from Smithy shape ``com.amazonaws.databrew#DeleteRecipeVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_databrew.types.recipe_name
    import aws_sdk_databrew.types.recipe_version


class DeleteRecipeVersionResponse(TypedDict, closed=True):
    name: "aws_sdk_databrew.types.recipe_name.RecipeName"
    """<p>The name of the recipe that was deleted.</p>"""
    recipe_version: "aws_sdk_databrew.types.recipe_version.RecipeVersion"
    """<p>The version of the recipe that was deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRecipeVersionResponse) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["RecipeVersion"] = value["recipe_version"]
    return out


def deserialize_json(data: dict) -> DeleteRecipeVersionResponse:
    out: DeleteRecipeVersionResponse = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DeleteRecipeVersionResponse.name required")
    if "RecipeVersion" in data:
        out["recipe_version"] = data["RecipeVersion"]
    else:
        raise DeserializationError(
            "DeleteRecipeVersionResponse.recipe_version required"
        )
    return out

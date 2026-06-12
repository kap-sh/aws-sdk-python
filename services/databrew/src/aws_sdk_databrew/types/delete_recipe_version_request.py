"""Generated from Smithy shape ``com.amazonaws.databrew#DeleteRecipeVersionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_databrew.types.recipe_name
    import aws_sdk_databrew.types.recipe_version


class DeleteRecipeVersionRequest(TypedDict):
    name: "aws_sdk_databrew.types.recipe_name.RecipeName"
    """<p>The name of the recipe.</p>"""
    recipe_version: "aws_sdk_databrew.types.recipe_version.RecipeVersion"
    """<p>The version of the recipe to be deleted. You can specify a numeric versions (<code>X.Y</code>) or <code>LATEST_WORKING</code>. <code>LATEST_PUBLISHED</code> is not supported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRecipeVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteRecipeVersionRequest:
    out: DeleteRecipeVersionRequest = {}  # type: ignore[typeddict-item]
    return out

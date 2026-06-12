"""Generated from Smithy shape ``com.amazonaws.databrew#PublishRecipeRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_databrew.types.recipe_description
    import aws_sdk_databrew.types.recipe_name


class PublishRecipeRequest(TypedDict):
    description: NotRequired[
        "aws_sdk_databrew.types.recipe_description.RecipeDescription"
    ]
    """<p>A description of the recipe to be published, for this version of the recipe.</p>"""
    name: "aws_sdk_databrew.types.recipe_name.RecipeName"
    """<p>The name of the recipe to be published.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PublishRecipeRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> PublishRecipeRequest:
    out: PublishRecipeRequest = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    return out

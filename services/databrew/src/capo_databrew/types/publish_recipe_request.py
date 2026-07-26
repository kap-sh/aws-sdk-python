"""Generated from Smithy shape ``com.amazonaws.databrew#PublishRecipeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.recipe_description
    import capo_databrew.types.recipe_name


class PublishRecipeRequest(TypedDict, closed=True):
    description: NotRequired["capo_databrew.types.recipe_description.RecipeDescription"]
    """<p>A description of the recipe to be published, for this version of the recipe.</p>"""
    name: "capo_databrew.types.recipe_name.RecipeName"
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

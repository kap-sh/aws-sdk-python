"""Generated from Smithy shape ``com.amazonaws.databrew#UpdateRecipeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.recipe_description
    import capo_databrew.types.recipe_name
    import capo_databrew.types.recipe_step_list


class UpdateRecipeRequest(TypedDict, closed=True):
    description: NotRequired["capo_databrew.types.recipe_description.RecipeDescription"]
    """<p>A description of the recipe.</p>"""
    name: "capo_databrew.types.recipe_name.RecipeName"
    """<p>The name of the recipe to be updated.</p>"""
    steps: NotRequired["capo_databrew.types.recipe_step_list.RecipeStepList"]
    """<p>One or more steps to be performed by the recipe. Each step consists of an action, and the conditions under which the action should succeed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRecipeRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "steps" in value:
        import capo_databrew.types.recipe_step_list

        out["Steps"] = capo_databrew.types.recipe_step_list.serialize_json(
            value["steps"]
        )
    return out


def deserialize_json(data: dict) -> UpdateRecipeRequest:
    out: UpdateRecipeRequest = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Steps" in data:
        import capo_databrew.types.recipe_step_list

        out["steps"] = capo_databrew.types.recipe_step_list.deserialize_json(
            data["Steps"]
        )
    return out

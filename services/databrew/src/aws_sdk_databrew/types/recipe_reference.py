"""Generated from Smithy shape ``com.amazonaws.databrew#RecipeReference``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_databrew.types.recipe_name
    import aws_sdk_databrew.types.recipe_version


class RecipeReference(TypedDict):
    name: "aws_sdk_databrew.types.recipe_name.RecipeName"
    """<p>The name of the recipe.</p>"""
    recipe_version: NotRequired["aws_sdk_databrew.types.recipe_version.RecipeVersion"]
    """<p>The identifier for the version for the recipe. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecipeReference) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "recipe_version" in value:
        out["RecipeVersion"] = value["recipe_version"]
    return out


def deserialize_json(data: dict) -> RecipeReference:
    out: RecipeReference = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("RecipeReference.name required")
    if "RecipeVersion" in data:
        out["recipe_version"] = data["RecipeVersion"]
    return out

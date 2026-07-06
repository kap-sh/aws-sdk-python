"""Generated from Smithy shape ``com.amazonaws.databrew#DescribeRecipeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_databrew.types.recipe_name
    import aws_sdk_databrew.types.recipe_version


class DescribeRecipeRequest(TypedDict, closed=True):
    name: "aws_sdk_databrew.types.recipe_name.RecipeName"
    """<p>The name of the recipe to be described.</p>"""
    recipe_version: NotRequired["aws_sdk_databrew.types.recipe_version.RecipeVersion"]
    """<p>The recipe version identifier. If this parameter isn't specified, then the latest published version is returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeRecipeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeRecipeRequest:
    out: DescribeRecipeRequest = {}  # type: ignore[typeddict-item]
    return out

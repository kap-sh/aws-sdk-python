"""Generated from Smithy shape ``com.amazonaws.databrew#ListRecipesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_databrew.types.max_results100
    import aws_sdk_databrew.types.next_token
    import aws_sdk_databrew.types.recipe_version


class ListRecipesRequest(TypedDict, closed=True):
    max_results: NotRequired["aws_sdk_databrew.types.max_results100.MaxResults100"]
    """<p>The maximum number of results to return in this request. </p>"""
    next_token: NotRequired["aws_sdk_databrew.types.next_token.NextToken"]
    """<p>The token returned by a previous call to retrieve the next set of results.</p>"""
    recipe_version: NotRequired["aws_sdk_databrew.types.recipe_version.RecipeVersion"]
    """<p>Return only those recipes with a version identifier of <code>LATEST_WORKING</code> or <code>LATEST_PUBLISHED</code>. If <code>RecipeVersion</code> is omitted, <code>ListRecipes</code> returns all of the <code>LATEST_PUBLISHED</code> recipe versions.</p> <p>Valid values: <code>LATEST_WORKING</code> | <code>LATEST_PUBLISHED</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecipesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListRecipesRequest:
    out: ListRecipesRequest = {}  # type: ignore[typeddict-item]
    return out

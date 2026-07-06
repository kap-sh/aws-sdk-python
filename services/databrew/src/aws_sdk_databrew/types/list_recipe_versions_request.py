"""Generated from Smithy shape ``com.amazonaws.databrew#ListRecipeVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_databrew.types.max_results100
    import aws_sdk_databrew.types.next_token
    import aws_sdk_databrew.types.recipe_name


class ListRecipeVersionsRequest(TypedDict, closed=True):
    max_results: NotRequired["aws_sdk_databrew.types.max_results100.MaxResults100"]
    """<p>The maximum number of results to return in this request. </p>"""
    next_token: NotRequired["aws_sdk_databrew.types.next_token.NextToken"]
    """<p>The token returned by a previous call to retrieve the next set of results.</p>"""
    name: "aws_sdk_databrew.types.recipe_name.RecipeName"
    """<p>The name of the recipe for which to return version information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecipeVersionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListRecipeVersionsRequest:
    out: ListRecipeVersionsRequest = {}  # type: ignore[typeddict-item]
    return out

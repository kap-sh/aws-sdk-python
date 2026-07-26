"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListRecommenderRecipesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.list_recommender_recipes_request_max_results_integer
    import capo_customer_profiles.types.token


class ListRecommenderRecipesRequest(TypedDict, closed=True):
    max_results: NotRequired[
        "capo_customer_profiles.types.list_recommender_recipes_request_max_results_integer.ListRecommenderRecipesRequestMaxResultsInteger"
    ]
    """<p>The maximum number of recommender recipes to return in the response. The default value is 100.</p>"""
    next_token: NotRequired["capo_customer_profiles.types.token.token"]
    """<p>A token received from a previous ListRecommenderRecipes call to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecommenderRecipesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListRecommenderRecipesRequest:
    out: ListRecommenderRecipesRequest = {}  # type: ignore[typeddict-item]
    return out

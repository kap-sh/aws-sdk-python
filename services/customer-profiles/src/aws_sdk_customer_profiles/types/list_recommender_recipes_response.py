"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListRecommenderRecipesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.recommender_recipes_list
    import aws_sdk_customer_profiles.types.token


class ListRecommenderRecipesResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_customer_profiles.types.token.token"]
    """<p>A token to retrieve the next page of results. Null if there are no more results to retrieve.</p>"""
    recommender_recipes: NotRequired[
        "aws_sdk_customer_profiles.types.recommender_recipes_list.RecommenderRecipesList"
    ]
    """<p>A list of available recommender recipes and their properties.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecommenderRecipesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "recommender_recipes" in value:
        import aws_sdk_customer_profiles.types.recommender_recipes_list

        out["RecommenderRecipes"] = (
            aws_sdk_customer_profiles.types.recommender_recipes_list.serialize_json(
                value["recommender_recipes"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListRecommenderRecipesResponse:
    out: ListRecommenderRecipesResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "RecommenderRecipes" in data:
        import aws_sdk_customer_profiles.types.recommender_recipes_list

        out["recommender_recipes"] = (
            aws_sdk_customer_profiles.types.recommender_recipes_list.deserialize_json(
                data["RecommenderRecipes"]
            )
        )
    return out

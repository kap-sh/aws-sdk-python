"""Generated from Smithy shape ``com.amazonaws.personalize#ListRecipesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.domain
    import capo_personalize.types.max_results
    import capo_personalize.types.next_token
    import capo_personalize.types.recipe_provider


class ListRecipesRequest(TypedDict, closed=True):
    recipe_provider: NotRequired[
        "capo_personalize.types.recipe_provider.RecipeProvider"
    ]
    """<p>The default is <code>SERVICE</code>.</p>"""
    next_token: NotRequired["capo_personalize.types.next_token.NextToken"]
    """<p>A token returned from the previous call to <code>ListRecipes</code> for getting the next set of recipes (if they exist).</p>"""
    max_results: NotRequired["capo_personalize.types.max_results.MaxResults"]
    """<p>The maximum number of recipes to return.</p>"""
    domain: NotRequired["capo_personalize.types.domain.Domain"]
    """<p> Filters returned recipes by domain for a Domain dataset group. Only recipes (Domain dataset group use cases) for this domain are included in the response. If you don't specify a domain, all recipes are returned. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListRecipesRequest) -> dict:
    out: dict = {}
    if "recipe_provider" in value:
        import capo_personalize.types.recipe_provider

        out["recipeProvider"] = (
            capo_personalize.types.recipe_provider.serialize_aws_json_1_1(
                value["recipe_provider"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "domain" in value:
        import capo_personalize.types.domain

        out["domain"] = capo_personalize.types.domain.serialize_aws_json_1_1(
            value["domain"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListRecipesRequest:
    out: ListRecipesRequest = {}  # type: ignore[typeddict-item]
    if "recipeProvider" in data:
        import capo_personalize.types.recipe_provider

        out["recipe_provider"] = (
            capo_personalize.types.recipe_provider.deserialize_aws_json_1_1(
                data["recipeProvider"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "domain" in data:
        import capo_personalize.types.domain

        out["domain"] = capo_personalize.types.domain.deserialize_aws_json_1_1(
            data["domain"]
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.personalize#ListRecipesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.next_token
    import capo_personalize.types.recipes


class ListRecipesResponse(TypedDict, closed=True):
    recipes: NotRequired["capo_personalize.types.recipes.Recipes"]
    """<p>The list of available recipes.</p>"""
    next_token: NotRequired["capo_personalize.types.next_token.NextToken"]
    """<p>A token for getting the next set of recipes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListRecipesResponse) -> dict:
    out: dict = {}
    if "recipes" in value:
        import capo_personalize.types.recipes

        out["recipes"] = capo_personalize.types.recipes.serialize_aws_json_1_1(
            value["recipes"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListRecipesResponse:
    out: ListRecipesResponse = {}  # type: ignore[typeddict-item]
    if "recipes" in data:
        import capo_personalize.types.recipes

        out["recipes"] = capo_personalize.types.recipes.deserialize_aws_json_1_1(
            data["recipes"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out

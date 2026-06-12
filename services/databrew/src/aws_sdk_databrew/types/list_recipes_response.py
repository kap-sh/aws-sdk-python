"""Generated from Smithy shape ``com.amazonaws.databrew#ListRecipesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_databrew.types.next_token
    import aws_sdk_databrew.types.recipe_list


class ListRecipesResponse(TypedDict):
    recipes: "aws_sdk_databrew.types.recipe_list.RecipeList"
    """<p>A list of recipes that are defined.</p>"""
    next_token: NotRequired["aws_sdk_databrew.types.next_token.NextToken"]
    """<p>A token that you can use in a subsequent call to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecipesResponse) -> dict:
    out: dict = {}
    import aws_sdk_databrew.types.recipe_list

    out["Recipes"] = aws_sdk_databrew.types.recipe_list.serialize_json(value["recipes"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRecipesResponse:
    out: ListRecipesResponse = {}  # type: ignore[typeddict-item]
    if "Recipes" in data:
        import aws_sdk_databrew.types.recipe_list

        out["recipes"] = aws_sdk_databrew.types.recipe_list.deserialize_json(
            data["Recipes"]
        )
    else:
        raise DeserializationError("ListRecipesResponse.recipes required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

"""Generated from Smithy shape ``com.amazonaws.databrew#ListRecipeVersionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_databrew.types.next_token
    import aws_sdk_databrew.types.recipe_list


class ListRecipeVersionsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_databrew.types.next_token.NextToken"]
    """<p>A token that you can use in a subsequent call to retrieve the next set of results.</p>"""
    recipes: "aws_sdk_databrew.types.recipe_list.RecipeList"
    """<p>A list of versions for the specified recipe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecipeVersionsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    import aws_sdk_databrew.types.recipe_list

    out["Recipes"] = aws_sdk_databrew.types.recipe_list.serialize_json(value["recipes"])
    return out


def deserialize_json(data: dict) -> ListRecipeVersionsResponse:
    out: ListRecipeVersionsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Recipes" in data:
        import aws_sdk_databrew.types.recipe_list

        out["recipes"] = aws_sdk_databrew.types.recipe_list.deserialize_json(
            data["Recipes"]
        )
    else:
        raise DeserializationError("ListRecipeVersionsResponse.recipes required")
    return out

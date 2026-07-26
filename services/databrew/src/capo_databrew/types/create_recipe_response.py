"""Generated from Smithy shape ``com.amazonaws.databrew#CreateRecipeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import capo_databrew.types.recipe_name


class CreateRecipeResponse(TypedDict, closed=True):
    name: "capo_databrew.types.recipe_name.RecipeName"
    """<p>The name of the recipe that you created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRecipeResponse) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> CreateRecipeResponse:
    out: CreateRecipeResponse = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateRecipeResponse.name required")
    return out

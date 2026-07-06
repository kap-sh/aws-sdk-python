"""Generated from Smithy shape ``com.amazonaws.databrew#UpdateRecipeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_databrew.types.recipe_name


class UpdateRecipeResponse(TypedDict, closed=True):
    name: "aws_sdk_databrew.types.recipe_name.RecipeName"
    """<p>The name of the recipe that was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRecipeResponse) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> UpdateRecipeResponse:
    out: UpdateRecipeResponse = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateRecipeResponse.name required")
    return out

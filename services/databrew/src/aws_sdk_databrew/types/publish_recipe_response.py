"""Generated from Smithy shape ``com.amazonaws.databrew#PublishRecipeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_databrew.types.recipe_name


class PublishRecipeResponse(TypedDict, closed=True):
    name: "aws_sdk_databrew.types.recipe_name.RecipeName"
    """<p>The name of the recipe that you published.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PublishRecipeResponse) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> PublishRecipeResponse:
    out: PublishRecipeResponse = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("PublishRecipeResponse.name required")
    return out

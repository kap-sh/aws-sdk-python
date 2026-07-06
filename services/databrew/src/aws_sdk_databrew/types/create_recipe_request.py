"""Generated from Smithy shape ``com.amazonaws.databrew#CreateRecipeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_databrew.types.recipe_description
    import aws_sdk_databrew.types.recipe_name
    import aws_sdk_databrew.types.recipe_step_list
    import aws_sdk_databrew.types.tag_map


class CreateRecipeRequest(TypedDict, closed=True):
    description: NotRequired[
        "aws_sdk_databrew.types.recipe_description.RecipeDescription"
    ]
    """<p>A description for the recipe.</p>"""
    name: "aws_sdk_databrew.types.recipe_name.RecipeName"
    """<p>A unique name for the recipe. Valid characters are alphanumeric (A-Z, a-z, 0-9), hyphen (-), period (.), and space.</p>"""
    steps: "aws_sdk_databrew.types.recipe_step_list.RecipeStepList"
    """<p>An array containing the steps to be performed by the recipe. Each recipe step consists of one recipe action and (optionally) an array of condition expressions.</p>"""
    tags: NotRequired["aws_sdk_databrew.types.tag_map.TagMap"]
    """<p>Metadata tags to apply to this recipe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRecipeRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    out["Name"] = value["name"]
    import aws_sdk_databrew.types.recipe_step_list

    out["Steps"] = aws_sdk_databrew.types.recipe_step_list.serialize_json(
        value["steps"]
    )
    if "tags" in value:
        import aws_sdk_databrew.types.tag_map

        out["Tags"] = aws_sdk_databrew.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateRecipeRequest:
    out: CreateRecipeRequest = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateRecipeRequest.name required")
    if "Steps" in data:
        import aws_sdk_databrew.types.recipe_step_list

        out["steps"] = aws_sdk_databrew.types.recipe_step_list.deserialize_json(
            data["Steps"]
        )
    else:
        raise DeserializationError("CreateRecipeRequest.steps required")
    if "Tags" in data:
        import aws_sdk_databrew.types.tag_map

        out["tags"] = aws_sdk_databrew.types.tag_map.deserialize_json(data["Tags"])
    return out

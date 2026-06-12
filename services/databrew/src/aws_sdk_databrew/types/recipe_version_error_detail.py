"""Generated from Smithy shape ``com.amazonaws.databrew#RecipeVersionErrorDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_databrew.types.error_code
    import aws_sdk_databrew.types.recipe_error_message
    import aws_sdk_databrew.types.recipe_version


class RecipeVersionErrorDetail(TypedDict):
    error_code: NotRequired["aws_sdk_databrew.types.error_code.ErrorCode"]
    """<p>The HTTP status code for the error.</p>"""
    error_message: NotRequired[
        "aws_sdk_databrew.types.recipe_error_message.RecipeErrorMessage"
    ]
    """<p>The text of the error message.</p>"""
    recipe_version: NotRequired["aws_sdk_databrew.types.recipe_version.RecipeVersion"]
    """<p>The identifier for the recipe version associated with this error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecipeVersionErrorDetail) -> dict:
    out: dict = {}
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "recipe_version" in value:
        out["RecipeVersion"] = value["recipe_version"]
    return out


def deserialize_json(data: dict) -> RecipeVersionErrorDetail:
    out: RecipeVersionErrorDetail = {}  # type: ignore[typeddict-item]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    if "RecipeVersion" in data:
        out["recipe_version"] = data["RecipeVersion"]
    return out

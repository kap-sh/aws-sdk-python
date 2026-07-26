"""Generated from Smithy shape ``com.amazonaws.databrew#RecipeVersionErrorDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.error_code
    import capo_databrew.types.recipe_error_message
    import capo_databrew.types.recipe_version


class RecipeVersionErrorDetail(TypedDict, closed=True):
    error_code: NotRequired["capo_databrew.types.error_code.ErrorCode"]
    """<p>The HTTP status code for the error.</p>"""
    error_message: NotRequired[
        "capo_databrew.types.recipe_error_message.RecipeErrorMessage"
    ]
    """<p>The text of the error message.</p>"""
    recipe_version: NotRequired["capo_databrew.types.recipe_version.RecipeVersion"]
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

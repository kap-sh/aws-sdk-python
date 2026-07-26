"""Generated from Smithy shape ``com.amazonaws.imagebuilder#DeleteImageRecipeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.image_recipe_arn
    import capo_imagebuilder.types.non_empty_string


class DeleteImageRecipeResponse(TypedDict, closed=True):
    request_id: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The request ID that uniquely identifies this request.</p>"""
    image_recipe_arn: NotRequired[
        "capo_imagebuilder.types.image_recipe_arn.ImageRecipeArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the image recipe that was deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteImageRecipeResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "image_recipe_arn" in value:
        out["imageRecipeArn"] = value["image_recipe_arn"]
    return out


def deserialize_json(data: dict) -> DeleteImageRecipeResponse:
    out: DeleteImageRecipeResponse = {}  # type: ignore[typeddict-item]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "imageRecipeArn" in data:
        out["image_recipe_arn"] = data["imageRecipeArn"]
    return out

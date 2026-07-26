"""Generated from Smithy shape ``com.amazonaws.imagebuilder#DeleteImageRecipeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.image_recipe_arn


class DeleteImageRecipeRequest(TypedDict, closed=True):
    image_recipe_arn: "capo_imagebuilder.types.image_recipe_arn.ImageRecipeArn"
    """<p>The Amazon Resource Name (ARN) of the image recipe to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteImageRecipeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteImageRecipeRequest:
    out: DeleteImageRecipeRequest = {}  # type: ignore[typeddict-item]
    return out

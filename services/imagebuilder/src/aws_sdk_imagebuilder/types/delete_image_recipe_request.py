"""Generated from Smithy shape ``com.amazonaws.imagebuilder#DeleteImageRecipeRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.image_recipe_arn


class DeleteImageRecipeRequest(TypedDict):
    image_recipe_arn: "aws_sdk_imagebuilder.types.image_recipe_arn.ImageRecipeArn"
    """<p>The Amazon Resource Name (ARN) of the image recipe to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteImageRecipeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteImageRecipeRequest:
    out: DeleteImageRecipeRequest = {}  # type: ignore[typeddict-item]
    return out

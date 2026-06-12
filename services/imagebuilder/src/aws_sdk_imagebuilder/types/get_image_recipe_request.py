"""Generated from Smithy shape ``com.amazonaws.imagebuilder#GetImageRecipeRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.image_recipe_arn


class GetImageRecipeRequest(TypedDict):
    image_recipe_arn: "aws_sdk_imagebuilder.types.image_recipe_arn.ImageRecipeArn"
    """<p>The Amazon Resource Name (ARN) of the image recipe that you want to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetImageRecipeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetImageRecipeRequest:
    out: GetImageRecipeRequest = {}  # type: ignore[typeddict-item]
    return out

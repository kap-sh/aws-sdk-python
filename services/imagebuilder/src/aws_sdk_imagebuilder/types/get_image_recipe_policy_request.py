"""Generated from Smithy shape ``com.amazonaws.imagebuilder#GetImageRecipePolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.image_recipe_arn


class GetImageRecipePolicyRequest(TypedDict):
    image_recipe_arn: "aws_sdk_imagebuilder.types.image_recipe_arn.ImageRecipeArn"
    """<p>The Amazon Resource Name (ARN) of the image recipe whose policy you want to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetImageRecipePolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetImageRecipePolicyRequest:
    out: GetImageRecipePolicyRequest = {}  # type: ignore[typeddict-item]
    return out

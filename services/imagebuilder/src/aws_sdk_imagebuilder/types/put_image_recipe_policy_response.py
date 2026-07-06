"""Generated from Smithy shape ``com.amazonaws.imagebuilder#PutImageRecipePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.image_recipe_arn
    import aws_sdk_imagebuilder.types.non_empty_string


class PutImageRecipePolicyResponse(TypedDict, closed=True):
    request_id: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The request ID that uniquely identifies this request.</p>"""
    image_recipe_arn: NotRequired[
        "aws_sdk_imagebuilder.types.image_recipe_arn.ImageRecipeArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the image recipe that this policy was applied to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutImageRecipePolicyResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "image_recipe_arn" in value:
        out["imageRecipeArn"] = value["image_recipe_arn"]
    return out


def deserialize_json(data: dict) -> PutImageRecipePolicyResponse:
    out: PutImageRecipePolicyResponse = {}  # type: ignore[typeddict-item]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "imageRecipeArn" in data:
        out["image_recipe_arn"] = data["imageRecipeArn"]
    return out

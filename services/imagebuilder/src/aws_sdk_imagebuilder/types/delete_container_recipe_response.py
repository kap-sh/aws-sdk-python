"""Generated from Smithy shape ``com.amazonaws.imagebuilder#DeleteContainerRecipeResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.container_recipe_arn
    import aws_sdk_imagebuilder.types.non_empty_string


class DeleteContainerRecipeResponse(TypedDict):
    request_id: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The request ID that uniquely identifies this request.</p>"""
    container_recipe_arn: NotRequired[
        "aws_sdk_imagebuilder.types.container_recipe_arn.ContainerRecipeArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the container recipe that was deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteContainerRecipeResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "container_recipe_arn" in value:
        out["containerRecipeArn"] = value["container_recipe_arn"]
    return out


def deserialize_json(data: dict) -> DeleteContainerRecipeResponse:
    out: DeleteContainerRecipeResponse = {}  # type: ignore[typeddict-item]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "containerRecipeArn" in data:
        out["container_recipe_arn"] = data["containerRecipeArn"]
    return out

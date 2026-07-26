"""Generated from Smithy shape ``com.amazonaws.imagebuilder#PutContainerRecipePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.container_recipe_arn
    import capo_imagebuilder.types.non_empty_string


class PutContainerRecipePolicyResponse(TypedDict, closed=True):
    request_id: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The request ID that uniquely identifies this request.</p>"""
    container_recipe_arn: NotRequired[
        "capo_imagebuilder.types.container_recipe_arn.ContainerRecipeArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the container recipe that this policy was applied to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutContainerRecipePolicyResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "container_recipe_arn" in value:
        out["containerRecipeArn"] = value["container_recipe_arn"]
    return out


def deserialize_json(data: dict) -> PutContainerRecipePolicyResponse:
    out: PutContainerRecipePolicyResponse = {}  # type: ignore[typeddict-item]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "containerRecipeArn" in data:
        out["container_recipe_arn"] = data["containerRecipeArn"]
    return out

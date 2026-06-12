"""Generated from Smithy shape ``com.amazonaws.imagebuilder#GetContainerRecipeRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.container_recipe_arn


class GetContainerRecipeRequest(TypedDict):
    container_recipe_arn: (
        "aws_sdk_imagebuilder.types.container_recipe_arn.ContainerRecipeArn"
    )
    """<p>The Amazon Resource Name (ARN) of the container recipe to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetContainerRecipeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetContainerRecipeRequest:
    out: GetContainerRecipeRequest = {}  # type: ignore[typeddict-item]
    return out

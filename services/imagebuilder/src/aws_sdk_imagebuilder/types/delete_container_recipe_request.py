"""Generated from Smithy shape ``com.amazonaws.imagebuilder#DeleteContainerRecipeRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.container_recipe_arn


class DeleteContainerRecipeRequest(TypedDict):
    container_recipe_arn: (
        "aws_sdk_imagebuilder.types.container_recipe_arn.ContainerRecipeArn"
    )
    """<p>The Amazon Resource Name (ARN) of the container recipe to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteContainerRecipeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteContainerRecipeRequest:
    out: DeleteContainerRecipeRequest = {}  # type: ignore[typeddict-item]
    return out

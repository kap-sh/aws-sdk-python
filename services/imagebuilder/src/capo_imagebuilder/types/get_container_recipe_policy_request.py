"""Generated from Smithy shape ``com.amazonaws.imagebuilder#GetContainerRecipePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.container_recipe_arn


class GetContainerRecipePolicyRequest(TypedDict, closed=True):
    container_recipe_arn: (
        "capo_imagebuilder.types.container_recipe_arn.ContainerRecipeArn"
    )
    """<p>The Amazon Resource Name (ARN) of the container recipe for the policy being requested.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetContainerRecipePolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetContainerRecipePolicyRequest:
    out: GetContainerRecipePolicyRequest = {}  # type: ignore[typeddict-item]
    return out

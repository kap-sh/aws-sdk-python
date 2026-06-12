"""Generated from Smithy shape ``com.amazonaws.imagebuilder#PutContainerRecipePolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.container_recipe_arn
    import aws_sdk_imagebuilder.types.resource_policy_document


class PutContainerRecipePolicyRequest(TypedDict):
    container_recipe_arn: (
        "aws_sdk_imagebuilder.types.container_recipe_arn.ContainerRecipeArn"
    )
    """<p>The Amazon Resource Name (ARN) of the container recipe that this policy should be applied to.</p>"""
    policy: "aws_sdk_imagebuilder.types.resource_policy_document.ResourcePolicyDocument"
    """<p>The policy to apply to the container recipe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutContainerRecipePolicyRequest) -> dict:
    out: dict = {}
    out["containerRecipeArn"] = value["container_recipe_arn"]
    out["policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> PutContainerRecipePolicyRequest:
    out: PutContainerRecipePolicyRequest = {}  # type: ignore[typeddict-item]
    if "containerRecipeArn" in data:
        out["container_recipe_arn"] = data["containerRecipeArn"]
    else:
        raise DeserializationError(
            "PutContainerRecipePolicyRequest.container_recipe_arn required"
        )
    if "policy" in data:
        out["policy"] = data["policy"]
    else:
        raise DeserializationError("PutContainerRecipePolicyRequest.policy required")
    return out

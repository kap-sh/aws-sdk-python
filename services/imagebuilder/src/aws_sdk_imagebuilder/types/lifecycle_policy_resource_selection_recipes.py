"""Generated from Smithy shape ``com.amazonaws.imagebuilder#LifecyclePolicyResourceSelectionRecipes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.lifecycle_policy_resource_selection_recipe

LifecyclePolicyResourceSelectionRecipes: TypeAlias = list[
    "aws_sdk_imagebuilder.types.lifecycle_policy_resource_selection_recipe.LifecyclePolicyResourceSelectionRecipe"
]


# --- restJson1 ser/de ---
def serialize_json(value: LifecyclePolicyResourceSelectionRecipes) -> list:
    import aws_sdk_imagebuilder.types.lifecycle_policy_resource_selection_recipe

    out: list = []
    for item in value:
        out.append(
            aws_sdk_imagebuilder.types.lifecycle_policy_resource_selection_recipe.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> LifecyclePolicyResourceSelectionRecipes:
    import aws_sdk_imagebuilder.types.lifecycle_policy_resource_selection_recipe

    out: LifecyclePolicyResourceSelectionRecipes = []
    for item in data:
        out.append(
            aws_sdk_imagebuilder.types.lifecycle_policy_resource_selection_recipe.deserialize_json(
                item
            )
        )
    return out

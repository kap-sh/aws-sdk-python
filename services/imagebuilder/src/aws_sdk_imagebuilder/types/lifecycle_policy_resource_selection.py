"""Generated from Smithy shape ``com.amazonaws.imagebuilder#LifecyclePolicyResourceSelection``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.lifecycle_policy_resource_selection_recipes
    import aws_sdk_imagebuilder.types.tag_map


class LifecyclePolicyResourceSelection(TypedDict):
    recipes: NotRequired[
        "aws_sdk_imagebuilder.types.lifecycle_policy_resource_selection_recipes.LifecyclePolicyResourceSelectionRecipes"
    ]
    """<p>A list of recipes that are used as selection criteria for the output images that the lifecycle policy applies to.</p>"""
    tag_map: NotRequired["aws_sdk_imagebuilder.types.tag_map.TagMap"]
    """<p>A list of tags that are used as selection criteria for the Image Builder image resources that the lifecycle policy applies to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LifecyclePolicyResourceSelection) -> dict:
    out: dict = {}
    if "recipes" in value:
        import aws_sdk_imagebuilder.types.lifecycle_policy_resource_selection_recipes

        out["recipes"] = (
            aws_sdk_imagebuilder.types.lifecycle_policy_resource_selection_recipes.serialize_json(
                value["recipes"]
            )
        )
    if "tag_map" in value:
        import aws_sdk_imagebuilder.types.tag_map

        out["tagMap"] = aws_sdk_imagebuilder.types.tag_map.serialize_json(
            value["tag_map"]
        )
    return out


def deserialize_json(data: dict) -> LifecyclePolicyResourceSelection:
    out: LifecyclePolicyResourceSelection = {}  # type: ignore[typeddict-item]
    if "recipes" in data:
        import aws_sdk_imagebuilder.types.lifecycle_policy_resource_selection_recipes

        out["recipes"] = (
            aws_sdk_imagebuilder.types.lifecycle_policy_resource_selection_recipes.deserialize_json(
                data["recipes"]
            )
        )
    if "tagMap" in data:
        import aws_sdk_imagebuilder.types.tag_map

        out["tag_map"] = aws_sdk_imagebuilder.types.tag_map.deserialize_json(
            data["tagMap"]
        )
    return out

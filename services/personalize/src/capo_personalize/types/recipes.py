"""Generated from Smithy shape ``com.amazonaws.personalize#Recipes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_personalize.types.recipe_summary

Recipes: TypeAlias = list["capo_personalize.types.recipe_summary.RecipeSummary"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Recipes) -> list:
    import capo_personalize.types.recipe_summary

    out: list = []
    for item in value:
        out.append(capo_personalize.types.recipe_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Recipes:
    import capo_personalize.types.recipe_summary

    out: Recipes = []
    for item in data:
        out.append(capo_personalize.types.recipe_summary.deserialize_aws_json_1_1(item))
    return out

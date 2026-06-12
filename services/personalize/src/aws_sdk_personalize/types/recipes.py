"""Generated from Smithy shape ``com.amazonaws.personalize#Recipes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_personalize.types.recipe_summary

Recipes: TypeAlias = list["aws_sdk_personalize.types.recipe_summary.RecipeSummary"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Recipes) -> list:
    import aws_sdk_personalize.types.recipe_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_personalize.types.recipe_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> Recipes:
    import aws_sdk_personalize.types.recipe_summary

    out: Recipes = []
    for item in data:
        out.append(
            aws_sdk_personalize.types.recipe_summary.deserialize_aws_json_1_1(item)
        )
    return out

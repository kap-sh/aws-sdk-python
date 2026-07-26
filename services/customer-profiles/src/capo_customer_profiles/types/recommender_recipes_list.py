"""Generated from Smithy shape ``com.amazonaws.customerprofiles#RecommenderRecipesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.recommender_recipe

RecommenderRecipesList: TypeAlias = list[
    "capo_customer_profiles.types.recommender_recipe.RecommenderRecipe"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommenderRecipesList) -> list:
    import capo_customer_profiles.types.recommender_recipe

    out: list = []
    for item in value:
        out.append(capo_customer_profiles.types.recommender_recipe.serialize_json(item))
    return out


def deserialize_json(data: list) -> RecommenderRecipesList:
    import capo_customer_profiles.types.recommender_recipe

    out: RecommenderRecipesList = []
    for item in data:
        out.append(
            capo_customer_profiles.types.recommender_recipe.deserialize_json(item)
        )
    return out

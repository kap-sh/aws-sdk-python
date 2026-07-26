"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#MachineLearningProductVisibilityFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.machine_learning_product_visibility_string

MachineLearningProductVisibilityFilterValueList: TypeAlias = list[
    "capo_marketplace_catalog.types.machine_learning_product_visibility_string.MachineLearningProductVisibilityString"
]


# --- restJson1 ser/de ---
def serialize_json(value: MachineLearningProductVisibilityFilterValueList) -> list:
    import capo_marketplace_catalog.types.machine_learning_product_visibility_string

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_catalog.types.machine_learning_product_visibility_string.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> MachineLearningProductVisibilityFilterValueList:
    import capo_marketplace_catalog.types.machine_learning_product_visibility_string

    out: MachineLearningProductVisibilityFilterValueList = []
    for item in data:
        out.append(
            capo_marketplace_catalog.types.machine_learning_product_visibility_string.deserialize_json(
                item
            )
        )
    return out

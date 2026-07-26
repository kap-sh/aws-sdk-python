"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#MachineLearningProductEntityIdFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.machine_learning_product_entity_id_string

MachineLearningProductEntityIdFilterValueList: TypeAlias = list[
    "capo_marketplace_catalog.types.machine_learning_product_entity_id_string.MachineLearningProductEntityIdString"
]


# --- restJson1 ser/de ---
def serialize_json(value: MachineLearningProductEntityIdFilterValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> MachineLearningProductEntityIdFilterValueList:
    return list(data)

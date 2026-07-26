"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#DataProductEntityIdFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.data_product_entity_id_string

DataProductEntityIdFilterValueList: TypeAlias = list[
    "capo_marketplace_catalog.types.data_product_entity_id_string.DataProductEntityIdString"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataProductEntityIdFilterValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> DataProductEntityIdFilterValueList:
    return list(data)

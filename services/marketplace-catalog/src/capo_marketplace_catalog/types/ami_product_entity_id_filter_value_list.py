"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#AmiProductEntityIdFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.ami_product_entity_id_string

AmiProductEntityIdFilterValueList: TypeAlias = list[
    "capo_marketplace_catalog.types.ami_product_entity_id_string.AmiProductEntityIdString"
]


# --- restJson1 ser/de ---
def serialize_json(value: AmiProductEntityIdFilterValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> AmiProductEntityIdFilterValueList:
    return list(data)

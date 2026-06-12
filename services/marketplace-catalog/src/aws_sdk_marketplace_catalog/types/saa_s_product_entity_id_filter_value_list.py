"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#SaaSProductEntityIdFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.saa_s_product_entity_id_string

SaaSProductEntityIdFilterValueList: TypeAlias = list[
    "aws_sdk_marketplace_catalog.types.saa_s_product_entity_id_string.SaaSProductEntityIdString"
]


# --- restJson1 ser/de ---
def serialize_json(value: SaaSProductEntityIdFilterValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> SaaSProductEntityIdFilterValueList:
    return list(data)

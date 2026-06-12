"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ContainerProductEntityIdFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.container_product_entity_id_string

ContainerProductEntityIdFilterValueList: TypeAlias = list[
    "aws_sdk_marketplace_catalog.types.container_product_entity_id_string.ContainerProductEntityIdString"
]


# --- restJson1 ser/de ---
def serialize_json(value: ContainerProductEntityIdFilterValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> ContainerProductEntityIdFilterValueList:
    return list(data)

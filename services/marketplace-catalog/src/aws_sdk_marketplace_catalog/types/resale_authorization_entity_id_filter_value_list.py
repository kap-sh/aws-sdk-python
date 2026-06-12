"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ResaleAuthorizationEntityIdFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.resale_authorization_entity_id_string

ResaleAuthorizationEntityIdFilterValueList: TypeAlias = list[
    "aws_sdk_marketplace_catalog.types.resale_authorization_entity_id_string.ResaleAuthorizationEntityIdString"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResaleAuthorizationEntityIdFilterValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> ResaleAuthorizationEntityIdFilterValueList:
    return list(data)

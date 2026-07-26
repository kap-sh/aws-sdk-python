"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ResaleAuthorizationProductIdFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.resale_authorization_product_id_string

ResaleAuthorizationProductIdFilterValueList: TypeAlias = list[
    "capo_marketplace_catalog.types.resale_authorization_product_id_string.ResaleAuthorizationProductIdString"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResaleAuthorizationProductIdFilterValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> ResaleAuthorizationProductIdFilterValueList:
    return list(data)

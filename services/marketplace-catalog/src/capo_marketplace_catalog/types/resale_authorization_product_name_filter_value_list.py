"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ResaleAuthorizationProductNameFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.resale_authorization_product_name_string

ResaleAuthorizationProductNameFilterValueList: TypeAlias = list[
    "capo_marketplace_catalog.types.resale_authorization_product_name_string.ResaleAuthorizationProductNameString"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResaleAuthorizationProductNameFilterValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> ResaleAuthorizationProductNameFilterValueList:
    return list(data)

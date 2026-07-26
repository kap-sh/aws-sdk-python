"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ResaleAuthorizationManufacturerAccountIdFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.resale_authorization_manufacturer_account_id_string

ResaleAuthorizationManufacturerAccountIdFilterValueList: TypeAlias = list[
    "capo_marketplace_catalog.types.resale_authorization_manufacturer_account_id_string.ResaleAuthorizationManufacturerAccountIdString"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: ResaleAuthorizationManufacturerAccountIdFilterValueList,
) -> list:
    return list(value)


def deserialize_json(
    data: list,
) -> ResaleAuthorizationManufacturerAccountIdFilterValueList:
    return list(data)

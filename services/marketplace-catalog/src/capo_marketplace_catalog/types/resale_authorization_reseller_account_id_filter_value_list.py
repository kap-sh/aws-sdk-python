"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ResaleAuthorizationResellerAccountIDFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.resale_authorization_reseller_account_id_string

ResaleAuthorizationResellerAccountIDFilterValueList: TypeAlias = list[
    "capo_marketplace_catalog.types.resale_authorization_reseller_account_id_string.ResaleAuthorizationResellerAccountIDString"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResaleAuthorizationResellerAccountIDFilterValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> ResaleAuthorizationResellerAccountIDFilterValueList:
    return list(data)

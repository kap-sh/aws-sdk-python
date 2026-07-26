"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ResaleAuthorizationResellerLegalNameFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.resale_authorization_reseller_legal_name_string

ResaleAuthorizationResellerLegalNameFilterValueList: TypeAlias = list[
    "capo_marketplace_catalog.types.resale_authorization_reseller_legal_name_string.ResaleAuthorizationResellerLegalNameString"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResaleAuthorizationResellerLegalNameFilterValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> ResaleAuthorizationResellerLegalNameFilterValueList:
    return list(data)

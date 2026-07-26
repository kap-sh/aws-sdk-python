"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ResaleAuthorizationNameFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.resale_authorization_name_string

ResaleAuthorizationNameFilterValueList: TypeAlias = list[
    "capo_marketplace_catalog.types.resale_authorization_name_string.ResaleAuthorizationNameString"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResaleAuthorizationNameFilterValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> ResaleAuthorizationNameFilterValueList:
    return list(data)

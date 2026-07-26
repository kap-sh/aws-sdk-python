"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ResaleAuthorizationStatusFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.resale_authorization_status_string

ResaleAuthorizationStatusFilterValueList: TypeAlias = list[
    "capo_marketplace_catalog.types.resale_authorization_status_string.ResaleAuthorizationStatusString"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResaleAuthorizationStatusFilterValueList) -> list:
    import capo_marketplace_catalog.types.resale_authorization_status_string

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_catalog.types.resale_authorization_status_string.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ResaleAuthorizationStatusFilterValueList:
    import capo_marketplace_catalog.types.resale_authorization_status_string

    out: ResaleAuthorizationStatusFilterValueList = []
    for item in data:
        out.append(
            capo_marketplace_catalog.types.resale_authorization_status_string.deserialize_json(
                item
            )
        )
    return out

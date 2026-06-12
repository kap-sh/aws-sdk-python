"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ResaleAuthorizationOfferExtendedStatusFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.resale_authorization_offer_extended_status_string

ResaleAuthorizationOfferExtendedStatusFilterValueList: TypeAlias = list[
    "aws_sdk_marketplace_catalog.types.resale_authorization_offer_extended_status_string.ResaleAuthorizationOfferExtendedStatusString"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: ResaleAuthorizationOfferExtendedStatusFilterValueList,
) -> list:
    return list(value)


def deserialize_json(
    data: list,
) -> ResaleAuthorizationOfferExtendedStatusFilterValueList:
    return list(data)

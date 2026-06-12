"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ResaleAuthorizationManufacturerLegalNameFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.resale_authorization_manufacturer_legal_name_string

ResaleAuthorizationManufacturerLegalNameFilterValueList: TypeAlias = list[
    "aws_sdk_marketplace_catalog.types.resale_authorization_manufacturer_legal_name_string.ResaleAuthorizationManufacturerLegalNameString"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: ResaleAuthorizationManufacturerLegalNameFilterValueList,
) -> list:
    return list(value)


def deserialize_json(
    data: list,
) -> ResaleAuthorizationManufacturerLegalNameFilterValueList:
    return list(data)

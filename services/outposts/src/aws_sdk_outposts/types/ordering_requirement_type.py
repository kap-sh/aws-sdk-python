"""Generated from Smithy shape ``com.amazonaws.outposts#OrderingRequirementType``."""

from typing import Literal, TypeAlias, cast

OrderingRequirementType: TypeAlias = Literal[
    "OUTPOST_ACTIVE_CHECK_ERROR",
    "MAXIMUM_ALLOWED_ORDERS_CHECK_ERROR",
    "VALID_ZIP_CODE_CHECK_ERROR",
    "RACK_PHYSICAL_PROPERTIES_CHECK_ERROR",
    "OPERATING_ADDRESS_EXISTENCE_CHECK_ERROR",
    "SHIPPING_ADDRESS_EXISTENCE_CHECK_ERROR",
    "COUNTRY_CODE_MISMATCH_CHECK_ERROR",
    "OUTPOST_GENERATION_MISMATCH_ERROR",
    "UNSUPPORTED",
    "OUTPOST_ID_MISSING_ON_QUOTE_ERROR",
    "ENTERPRISE_SUPPORT_ERROR",
    "SHIPPING_ADDRESS_MISSING_CONTACT_NAME_ERROR",
    "SHIPPING_ADDRESS_MISSING_CONTACT_NUMBER_ERROR",
    "SHIPPING_ADDRESS_MISSING_CONTACT_INFO_ERROR",
    "OUTPOST_STATE_CHANGED_ERROR",
    "OUTPOST_NOT_FOUND_ERROR",
    "OUTPOST_RENEWAL_REQUIRED_ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: OrderingRequirementType) -> str:
    return value


def deserialize_json(data: str) -> OrderingRequirementType:
    return cast(OrderingRequirementType, data)

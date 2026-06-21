"""Generated from Smithy shape ``com.amazonaws.taxsettings#AddressRoleType``."""

from typing import Literal, TypeAlias, cast

AddressRoleType: TypeAlias = Literal[
    "TaxAddress",
    "BillingAddress",
    "ContactAddress",
]


# --- restJson1 ser/de ---
def serialize_json(value: AddressRoleType) -> str:
    return value


def deserialize_json(data: str) -> AddressRoleType:
    return cast(AddressRoleType, data)

"""Generated from Smithy shape ``com.amazonaws.customerprofiles#AddressList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.string1_to255

AddressList: TypeAlias = list["capo_customer_profiles.types.string1_to255.string1To255"]


# --- restJson1 ser/de ---
def serialize_json(value: AddressList) -> list:
    return list(value)


def deserialize_json(data: list) -> AddressList:
    return list(data)

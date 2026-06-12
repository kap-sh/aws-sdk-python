"""Generated from Smithy shape ``com.amazonaws.customerprofiles#PhoneNumberList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.string1_to255

PhoneNumberList: TypeAlias = list[
    "aws_sdk_customer_profiles.types.string1_to255.string1To255"
]


# --- restJson1 ser/de ---
def serialize_json(value: PhoneNumberList) -> list:
    return list(value)


def deserialize_json(data: list) -> PhoneNumberList:
    return list(data)

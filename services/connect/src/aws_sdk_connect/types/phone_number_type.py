"""Generated from Smithy shape ``com.amazonaws.connect#PhoneNumberType``."""

from typing import Literal, TypeAlias, cast

PhoneNumberType: TypeAlias = Literal[
    "TOLL_FREE",
    "DID",
    "UIFN",
    "SHARED",
    "THIRD_PARTY_TF",
    "THIRD_PARTY_DID",
    "SHORT_CODE",
]


# --- restJson1 ser/de ---
def serialize_json(value: PhoneNumberType) -> str:
    return value


def deserialize_json(data: str) -> PhoneNumberType:
    return cast(PhoneNumberType, data)

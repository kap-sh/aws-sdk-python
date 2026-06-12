"""Generated from Smithy shape ``com.amazonaws.connect#PhoneNumberType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "TOLL_FREE",
        "DID",
        "UIFN",
        "SHARED",
        "THIRD_PARTY_TF",
        "THIRD_PARTY_DID",
        "SHORT_CODE",
    )
)


def serialize_json(value: PhoneNumberType) -> str:
    return value


def deserialize_json(data: str) -> PhoneNumberType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PhoneNumberType value: {data!r}")
    return cast(PhoneNumberType, data)

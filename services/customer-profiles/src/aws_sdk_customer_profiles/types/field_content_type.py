"""Generated from Smithy shape ``com.amazonaws.customerprofiles#FieldContentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_customer_profiles.errors import DeserializationError

FieldContentType: TypeAlias = Literal[
    "STRING",
    "NUMBER",
    "PHONE_NUMBER",
    "EMAIL_ADDRESS",
    "NAME",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STRING",
        "NUMBER",
        "PHONE_NUMBER",
        "EMAIL_ADDRESS",
        "NAME",
    )
)


def serialize_json(value: FieldContentType) -> str:
    return value


def deserialize_json(data: str) -> FieldContentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FieldContentType value: {data!r}")
    return cast(FieldContentType, data)

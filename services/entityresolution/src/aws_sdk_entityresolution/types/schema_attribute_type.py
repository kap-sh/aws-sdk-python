"""Generated from Smithy shape ``com.amazonaws.entityresolution#SchemaAttributeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_entityresolution.errors import DeserializationError

SchemaAttributeType: TypeAlias = Literal[
    "NAME",
    "NAME_FIRST",
    "NAME_MIDDLE",
    "NAME_LAST",
    "ADDRESS",
    "ADDRESS_STREET1",
    "ADDRESS_STREET2",
    "ADDRESS_STREET3",
    "ADDRESS_CITY",
    "ADDRESS_STATE",
    "ADDRESS_COUNTRY",
    "ADDRESS_POSTALCODE",
    "PHONE",
    "PHONE_NUMBER",
    "PHONE_COUNTRYCODE",
    "EMAIL_ADDRESS",
    "UNIQUE_ID",
    "DATE",
    "STRING",
    "PROVIDER_ID",
    "IPV4",
    "IPV6",
    "MAID",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NAME",
        "NAME_FIRST",
        "NAME_MIDDLE",
        "NAME_LAST",
        "ADDRESS",
        "ADDRESS_STREET1",
        "ADDRESS_STREET2",
        "ADDRESS_STREET3",
        "ADDRESS_CITY",
        "ADDRESS_STATE",
        "ADDRESS_COUNTRY",
        "ADDRESS_POSTALCODE",
        "PHONE",
        "PHONE_NUMBER",
        "PHONE_COUNTRYCODE",
        "EMAIL_ADDRESS",
        "UNIQUE_ID",
        "DATE",
        "STRING",
        "PROVIDER_ID",
        "IPV4",
        "IPV6",
        "MAID",
    )
)


def serialize_json(value: SchemaAttributeType) -> str:
    return value


def deserialize_json(data: str) -> SchemaAttributeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SchemaAttributeType value: {data!r}")
    return cast(SchemaAttributeType, data)

"""Generated from Smithy shape ``com.amazonaws.entityresolution#SchemaAttributeType``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: SchemaAttributeType) -> str:
    return value


def deserialize_json(data: str) -> SchemaAttributeType:
    return cast(SchemaAttributeType, data)

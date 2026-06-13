"""Generated from Smithy shape ``com.amazonaws.taxsettings#AddressRoleType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_taxsettings.errors import DeserializationError

AddressRoleType: TypeAlias = Literal[
    "TaxAddress",
    "BillingAddress",
    "ContactAddress",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TaxAddress",
        "BillingAddress",
        "ContactAddress",
    )
)


def serialize_json(value: AddressRoleType) -> str:
    return value


def deserialize_json(data: str) -> AddressRoleType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AddressRoleType value: {data!r}")
    return cast(AddressRoleType, data)

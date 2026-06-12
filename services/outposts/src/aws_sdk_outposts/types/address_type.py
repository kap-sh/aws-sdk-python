"""Generated from Smithy shape ``com.amazonaws.outposts#AddressType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_outposts.errors import DeserializationError

AddressType: TypeAlias = Literal[
    "SHIPPING_ADDRESS",
    "OPERATING_ADDRESS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SHIPPING_ADDRESS",
        "OPERATING_ADDRESS",
    )
)


def serialize_json(value: AddressType) -> str:
    return value


def deserialize_json(data: str) -> AddressType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AddressType value: {data!r}")
    return cast(AddressType, data)

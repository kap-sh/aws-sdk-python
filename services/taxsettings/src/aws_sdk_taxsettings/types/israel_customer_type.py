"""Generated from Smithy shape ``com.amazonaws.taxsettings#IsraelCustomerType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_taxsettings.errors import DeserializationError

IsraelCustomerType: TypeAlias = Literal[
    "Business",
    "Individual",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Business",
        "Individual",
    )
)


def serialize_json(value: IsraelCustomerType) -> str:
    return value


def deserialize_json(data: str) -> IsraelCustomerType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IsraelCustomerType value: {data!r}")
    return cast(IsraelCustomerType, data)

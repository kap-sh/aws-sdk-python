"""Generated from Smithy shape ``com.amazonaws.securityir#CustomerType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_security_ir.errors import DeserializationError

CustomerType: TypeAlias = Literal[
    "Standalone",
    "Organization",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Standalone",
        "Organization",
    )
)


def serialize_json(value: CustomerType) -> str:
    return value


def deserialize_json(data: str) -> CustomerType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CustomerType value: {data!r}")
    return cast(CustomerType, data)

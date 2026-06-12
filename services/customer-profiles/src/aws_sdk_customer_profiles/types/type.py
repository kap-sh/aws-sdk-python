"""Generated from Smithy shape ``com.amazonaws.customerprofiles#Type``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_customer_profiles.errors import DeserializationError

Type: TypeAlias = Literal[
    "ALL",
    "ANY",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL",
        "ANY",
        "NONE",
    )
)


def serialize_json(value: Type) -> str:
    return value


def deserialize_json(data: str) -> Type:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Type value: {data!r}")
    return cast(Type, data)

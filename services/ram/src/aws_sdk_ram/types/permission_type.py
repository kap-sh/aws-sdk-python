"""Generated from Smithy shape ``com.amazonaws.ram#PermissionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ram.errors import DeserializationError

PermissionType: TypeAlias = Literal[
    "CUSTOMER_MANAGED",
    "AWS_MANAGED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CUSTOMER_MANAGED",
        "AWS_MANAGED",
    )
)


def serialize_json(value: PermissionType) -> str:
    return value


def deserialize_json(data: str) -> PermissionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PermissionType value: {data!r}")
    return cast(PermissionType, data)

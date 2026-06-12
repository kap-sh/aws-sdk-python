"""Generated from Smithy shape ``com.amazonaws.ram#PermissionTypeFilter``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ram.errors import DeserializationError

PermissionTypeFilter: TypeAlias = Literal[
    "ALL",
    "AWS_MANAGED",
    "CUSTOMER_MANAGED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL",
        "AWS_MANAGED",
        "CUSTOMER_MANAGED",
    )
)


def serialize_json(value: PermissionTypeFilter) -> str:
    return value


def deserialize_json(data: str) -> PermissionTypeFilter:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PermissionTypeFilter value: {data!r}")
    return cast(PermissionTypeFilter, data)

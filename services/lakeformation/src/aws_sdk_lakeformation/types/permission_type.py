"""Generated from Smithy shape ``com.amazonaws.lakeformation#PermissionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lakeformation.errors import DeserializationError

PermissionType: TypeAlias = Literal[
    "COLUMN_PERMISSION",
    "CELL_FILTER_PERMISSION",
    "NESTED_PERMISSION",
    "NESTED_CELL_PERMISSION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COLUMN_PERMISSION",
        "CELL_FILTER_PERMISSION",
        "NESTED_PERMISSION",
        "NESTED_CELL_PERMISSION",
    )
)


def serialize_json(value: PermissionType) -> str:
    return value


def deserialize_json(data: str) -> PermissionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PermissionType value: {data!r}")
    return cast(PermissionType, data)

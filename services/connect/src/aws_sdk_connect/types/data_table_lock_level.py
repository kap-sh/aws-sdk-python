"""Generated from Smithy shape ``com.amazonaws.connect#DataTableLockLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

DataTableLockLevel: TypeAlias = Literal[
    "NONE",
    "DATA_TABLE",
    "PRIMARY_VALUE",
    "ATTRIBUTE",
    "VALUE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "DATA_TABLE",
        "PRIMARY_VALUE",
        "ATTRIBUTE",
        "VALUE",
    )
)


def serialize_json(value: DataTableLockLevel) -> str:
    return value


def deserialize_json(data: str) -> DataTableLockLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataTableLockLevel value: {data!r}")
    return cast(DataTableLockLevel, data)

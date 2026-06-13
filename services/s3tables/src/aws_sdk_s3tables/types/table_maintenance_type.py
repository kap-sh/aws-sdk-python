"""Generated from Smithy shape ``com.amazonaws.s3tables#TableMaintenanceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3tables.errors import DeserializationError

TableMaintenanceType: TypeAlias = Literal[
    "icebergCompaction",
    "icebergSnapshotManagement",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "icebergCompaction",
        "icebergSnapshotManagement",
    )
)


def serialize_json(value: TableMaintenanceType) -> str:
    return value


def deserialize_json(data: str) -> TableMaintenanceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TableMaintenanceType value: {data!r}")
    return cast(TableMaintenanceType, data)

"""Generated from Smithy shape ``com.amazonaws.s3tables#TableMaintenanceJobType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3tables.errors import DeserializationError

TableMaintenanceJobType: TypeAlias = Literal[
    "icebergCompaction",
    "icebergSnapshotManagement",
    "icebergUnreferencedFileRemoval",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "icebergCompaction",
        "icebergSnapshotManagement",
        "icebergUnreferencedFileRemoval",
    )
)


def serialize_json(value: TableMaintenanceJobType) -> str:
    return value


def deserialize_json(data: str) -> TableMaintenanceJobType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TableMaintenanceJobType value: {data!r}")
    return cast(TableMaintenanceJobType, data)

"""Generated from Smithy shape ``com.amazonaws.s3tables#TableMaintenanceJobType``."""

from typing import Literal, TypeAlias, cast

TableMaintenanceJobType: TypeAlias = Literal[
    "icebergCompaction",
    "icebergSnapshotManagement",
    "icebergUnreferencedFileRemoval",
]


# --- restJson1 ser/de ---
def serialize_json(value: TableMaintenanceJobType) -> str:
    return value


def deserialize_json(data: str) -> TableMaintenanceJobType:
    return cast(TableMaintenanceJobType, data)

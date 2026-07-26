"""Generated from Smithy shape ``com.amazonaws.s3tables#TableMaintenanceType``."""

from typing import Literal, TypeAlias, cast

TableMaintenanceType: TypeAlias = Literal[
    "icebergCompaction",
    "icebergSnapshotManagement",
]


# --- restJson1 ser/de ---
def serialize_json(value: TableMaintenanceType) -> str:
    return value


def deserialize_json(data: str) -> TableMaintenanceType:
    return cast(TableMaintenanceType, data)

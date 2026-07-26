"""Generated from Smithy shape ``com.amazonaws.s3tables#TableBucketMaintenanceType``."""

from typing import Literal, TypeAlias, cast

TableBucketMaintenanceType: TypeAlias = Literal["icebergUnreferencedFileRemoval",]


# --- restJson1 ser/de ---
def serialize_json(value: TableBucketMaintenanceType) -> str:
    return value


def deserialize_json(data: str) -> TableBucketMaintenanceType:
    return cast(TableBucketMaintenanceType, data)

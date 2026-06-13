"""Generated from Smithy shape ``com.amazonaws.s3tables#TableBucketMaintenanceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3tables.errors import DeserializationError

TableBucketMaintenanceType: TypeAlias = Literal["icebergUnreferencedFileRemoval",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("icebergUnreferencedFileRemoval",))


def serialize_json(value: TableBucketMaintenanceType) -> str:
    return value


def deserialize_json(data: str) -> TableBucketMaintenanceType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown TableBucketMaintenanceType value: {data!r}"
        )
    return cast(TableBucketMaintenanceType, data)

"""Generated from Smithy shape ``com.amazonaws.s3tables#TableMaintenanceSettings``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_s3tables.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.iceberg_compaction_settings
    import aws_sdk_s3tables.types.iceberg_snapshot_management_settings


class _TableMaintenanceSettings_icebergCompaction(TypedDict, closed=True):
    icebergCompaction: (
        "aws_sdk_s3tables.types.iceberg_compaction_settings.IcebergCompactionSettings"
    )


class _TableMaintenanceSettings_icebergSnapshotManagement(TypedDict, closed=True):
    icebergSnapshotManagement: "aws_sdk_s3tables.types.iceberg_snapshot_management_settings.IcebergSnapshotManagementSettings"


TableMaintenanceSettings: TypeAlias = (
    _TableMaintenanceSettings_icebergCompaction
    | _TableMaintenanceSettings_icebergSnapshotManagement
)


# --- restJson1 ser/de ---
def serialize_json(value: TableMaintenanceSettings) -> dict:
    if "icebergCompaction" in value:
        import aws_sdk_s3tables.types.iceberg_compaction_settings

        return {
            "icebergCompaction": aws_sdk_s3tables.types.iceberg_compaction_settings.serialize_json(
                value["icebergCompaction"]
            )
        }
    elif "icebergSnapshotManagement" in value:
        import aws_sdk_s3tables.types.iceberg_snapshot_management_settings

        return {
            "icebergSnapshotManagement": aws_sdk_s3tables.types.iceberg_snapshot_management_settings.serialize_json(
                value["icebergSnapshotManagement"]
            )
        }
    else:
        raise SerializationError("TableMaintenanceSettings: no variant present")


def deserialize_json(data: dict) -> TableMaintenanceSettings:
    if "icebergCompaction" in data:
        import aws_sdk_s3tables.types.iceberg_compaction_settings

        return {
            "icebergCompaction": aws_sdk_s3tables.types.iceberg_compaction_settings.deserialize_json(
                data["icebergCompaction"]
            )
        }
    elif "icebergSnapshotManagement" in data:
        import aws_sdk_s3tables.types.iceberg_snapshot_management_settings

        return {
            "icebergSnapshotManagement": aws_sdk_s3tables.types.iceberg_snapshot_management_settings.deserialize_json(
                data["icebergSnapshotManagement"]
            )
        }
    else:
        raise DeserializationError(
            "TableMaintenanceSettings: no recognized variant key"
        )

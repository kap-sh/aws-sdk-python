"""Generated from Smithy shape ``com.amazonaws.s3tables#TableBucketMaintenanceSettings``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_s3tables.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.iceberg_unreferenced_file_removal_settings


class _TableBucketMaintenanceSettings_icebergUnreferencedFileRemoval(
    TypedDict, closed=True
):
    icebergUnreferencedFileRemoval: "aws_sdk_s3tables.types.iceberg_unreferenced_file_removal_settings.IcebergUnreferencedFileRemovalSettings"


TableBucketMaintenanceSettings: TypeAlias = (
    _TableBucketMaintenanceSettings_icebergUnreferencedFileRemoval
)


# --- restJson1 ser/de ---
def serialize_json(value: TableBucketMaintenanceSettings) -> dict:
    if "icebergUnreferencedFileRemoval" in value:
        import aws_sdk_s3tables.types.iceberg_unreferenced_file_removal_settings

        return {
            "icebergUnreferencedFileRemoval": aws_sdk_s3tables.types.iceberg_unreferenced_file_removal_settings.serialize_json(
                value["icebergUnreferencedFileRemoval"]
            )
        }
    else:
        raise SerializationError("TableBucketMaintenanceSettings: no variant present")


def deserialize_json(data: dict) -> TableBucketMaintenanceSettings:
    if "icebergUnreferencedFileRemoval" in data:
        import aws_sdk_s3tables.types.iceberg_unreferenced_file_removal_settings

        return {
            "icebergUnreferencedFileRemoval": aws_sdk_s3tables.types.iceberg_unreferenced_file_removal_settings.deserialize_json(
                data["icebergUnreferencedFileRemoval"]
            )
        }
    else:
        raise DeserializationError(
            "TableBucketMaintenanceSettings: no recognized variant key"
        )

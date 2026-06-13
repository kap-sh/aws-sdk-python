"""Generated from Smithy shape ``com.amazonaws.s3tables#TableBucketMaintenanceConfigurationValue``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.maintenance_status
    import aws_sdk_s3tables.types.table_bucket_maintenance_settings


class TableBucketMaintenanceConfigurationValue(TypedDict):
    status: NotRequired["aws_sdk_s3tables.types.maintenance_status.MaintenanceStatus"]
    """<p>The status of the maintenance configuration.</p>"""
    settings: NotRequired[
        "aws_sdk_s3tables.types.table_bucket_maintenance_settings.TableBucketMaintenanceSettings"
    ]
    """<p>Contains details about the settings of the maintenance configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TableBucketMaintenanceConfigurationValue) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_s3tables.types.maintenance_status

        out["status"] = aws_sdk_s3tables.types.maintenance_status.serialize_json(
            value["status"]
        )
    if "settings" in value:
        import aws_sdk_s3tables.types.table_bucket_maintenance_settings

        out["settings"] = (
            aws_sdk_s3tables.types.table_bucket_maintenance_settings.serialize_json(
                value["settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> TableBucketMaintenanceConfigurationValue:
    out: TableBucketMaintenanceConfigurationValue = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_s3tables.types.maintenance_status

        out["status"] = aws_sdk_s3tables.types.maintenance_status.deserialize_json(
            data["status"]
        )
    if "settings" in data:
        import aws_sdk_s3tables.types.table_bucket_maintenance_settings

        out["settings"] = (
            aws_sdk_s3tables.types.table_bucket_maintenance_settings.deserialize_json(
                data["settings"]
            )
        )
    return out

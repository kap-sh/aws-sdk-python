"""Generated from Smithy shape ``com.amazonaws.s3tables#GetTableBucketMaintenanceConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_s3tables.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.table_bucket_arn
    import aws_sdk_s3tables.types.table_bucket_maintenance_configuration


class GetTableBucketMaintenanceConfigurationResponse(TypedDict):
    table_bucket_arn: "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN"
    """<p>The Amazon Resource Name (ARN) of the table bucket associated with the maintenance configuration.</p>"""
    configuration: "aws_sdk_s3tables.types.table_bucket_maintenance_configuration.TableBucketMaintenanceConfiguration"
    """<p>Details about the maintenance configuration for the table bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTableBucketMaintenanceConfigurationResponse) -> dict:
    out: dict = {}
    out["tableBucketARN"] = value["table_bucket_arn"]
    import aws_sdk_s3tables.types.table_bucket_maintenance_configuration

    out["configuration"] = (
        aws_sdk_s3tables.types.table_bucket_maintenance_configuration.serialize_json(
            value["configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetTableBucketMaintenanceConfigurationResponse:
    out: GetTableBucketMaintenanceConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "tableBucketARN" in data:
        out["table_bucket_arn"] = data["tableBucketARN"]
    else:
        raise DeserializationError(
            "GetTableBucketMaintenanceConfigurationResponse.table_bucket_arn required"
        )
    if "configuration" in data:
        import aws_sdk_s3tables.types.table_bucket_maintenance_configuration

        out["configuration"] = (
            aws_sdk_s3tables.types.table_bucket_maintenance_configuration.deserialize_json(
                data["configuration"]
            )
        )
    else:
        raise DeserializationError(
            "GetTableBucketMaintenanceConfigurationResponse.configuration required"
        )
    return out

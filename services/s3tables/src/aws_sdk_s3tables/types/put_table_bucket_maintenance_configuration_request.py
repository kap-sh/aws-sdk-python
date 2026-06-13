"""Generated from Smithy shape ``com.amazonaws.s3tables#PutTableBucketMaintenanceConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_s3tables.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.table_bucket_arn
    import aws_sdk_s3tables.types.table_bucket_maintenance_configuration_value
    import aws_sdk_s3tables.types.table_bucket_maintenance_type


class PutTableBucketMaintenanceConfigurationRequest(TypedDict):
    table_bucket_arn: "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN"
    """<p>The Amazon Resource Name (ARN) of the table bucket associated with the maintenance configuration.</p>"""
    type: "aws_sdk_s3tables.types.table_bucket_maintenance_type.TableBucketMaintenanceType"
    """<p>The type of the maintenance configuration.</p>"""
    value: "aws_sdk_s3tables.types.table_bucket_maintenance_configuration_value.TableBucketMaintenanceConfigurationValue"
    """<p>Defines the values of the maintenance configuration for the table bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutTableBucketMaintenanceConfigurationRequest) -> dict:
    out: dict = {}
    import aws_sdk_s3tables.types.table_bucket_maintenance_configuration_value

    out["value"] = (
        aws_sdk_s3tables.types.table_bucket_maintenance_configuration_value.serialize_json(
            value["value"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutTableBucketMaintenanceConfigurationRequest:
    out: PutTableBucketMaintenanceConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "value" in data:
        import aws_sdk_s3tables.types.table_bucket_maintenance_configuration_value

        out["value"] = (
            aws_sdk_s3tables.types.table_bucket_maintenance_configuration_value.deserialize_json(
                data["value"]
            )
        )
    else:
        raise DeserializationError(
            "PutTableBucketMaintenanceConfigurationRequest.value required"
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.s3tables#TableMaintenanceJobStatus``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.table_maintenance_job_status_value
    import aws_sdk_s3tables.types.table_maintenance_job_type

TableMaintenanceJobStatus: TypeAlias = dict[
    "aws_sdk_s3tables.types.table_maintenance_job_type.TableMaintenanceJobType",
    "aws_sdk_s3tables.types.table_maintenance_job_status_value.TableMaintenanceJobStatusValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: TableMaintenanceJobStatus) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_s3tables.types.table_maintenance_job_status_value
        import aws_sdk_s3tables.types.table_maintenance_job_type

        out[aws_sdk_s3tables.types.table_maintenance_job_type.serialize_json(key)] = (
            aws_sdk_s3tables.types.table_maintenance_job_status_value.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> TableMaintenanceJobStatus:
    out: TableMaintenanceJobStatus = {}
    for key, value in data.items():
        import aws_sdk_s3tables.types.table_maintenance_job_status_value
        import aws_sdk_s3tables.types.table_maintenance_job_type

        out[aws_sdk_s3tables.types.table_maintenance_job_type.deserialize_json(key)] = (
            aws_sdk_s3tables.types.table_maintenance_job_status_value.deserialize_json(
                value
            )
        )
    return out

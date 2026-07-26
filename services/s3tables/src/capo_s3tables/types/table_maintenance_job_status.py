"""Generated from Smithy shape ``com.amazonaws.s3tables#TableMaintenanceJobStatus``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_s3tables.types.table_maintenance_job_status_value
    import capo_s3tables.types.table_maintenance_job_type

TableMaintenanceJobStatus: TypeAlias = dict[
    "capo_s3tables.types.table_maintenance_job_type.TableMaintenanceJobType",
    "capo_s3tables.types.table_maintenance_job_status_value.TableMaintenanceJobStatusValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: TableMaintenanceJobStatus) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_s3tables.types.table_maintenance_job_status_value
        import capo_s3tables.types.table_maintenance_job_type

        out[capo_s3tables.types.table_maintenance_job_type.serialize_json(key)] = (
            capo_s3tables.types.table_maintenance_job_status_value.serialize_json(value)
        )
    return out


def deserialize_json(data: dict) -> TableMaintenanceJobStatus:
    out: TableMaintenanceJobStatus = {}
    for key, value in data.items():
        import capo_s3tables.types.table_maintenance_job_status_value
        import capo_s3tables.types.table_maintenance_job_type

        out[capo_s3tables.types.table_maintenance_job_type.deserialize_json(key)] = (
            capo_s3tables.types.table_maintenance_job_status_value.deserialize_json(
                value
            )
        )
    return out

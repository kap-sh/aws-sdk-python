"""Generated from Smithy shape ``com.amazonaws.s3tables#GetTableMaintenanceJobStatusResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_s3tables.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.table_arn
    import aws_sdk_s3tables.types.table_maintenance_job_status


class GetTableMaintenanceJobStatusResponse(TypedDict):
    table_arn: "aws_sdk_s3tables.types.table_arn.TableARN"
    """<p>The Amazon Resource Name (ARN) of the table.</p>"""
    status: (
        "aws_sdk_s3tables.types.table_maintenance_job_status.TableMaintenanceJobStatus"
    )
    """<p>The status of the maintenance job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTableMaintenanceJobStatusResponse) -> dict:
    out: dict = {}
    out["tableARN"] = value["table_arn"]
    import aws_sdk_s3tables.types.table_maintenance_job_status

    out["status"] = aws_sdk_s3tables.types.table_maintenance_job_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> GetTableMaintenanceJobStatusResponse:
    out: GetTableMaintenanceJobStatusResponse = {}  # type: ignore[typeddict-item]
    if "tableARN" in data:
        out["table_arn"] = data["tableARN"]
    else:
        raise DeserializationError(
            "GetTableMaintenanceJobStatusResponse.table_arn required"
        )
    if "status" in data:
        import aws_sdk_s3tables.types.table_maintenance_job_status

        out["status"] = (
            aws_sdk_s3tables.types.table_maintenance_job_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError(
            "GetTableMaintenanceJobStatusResponse.status required"
        )
    return out

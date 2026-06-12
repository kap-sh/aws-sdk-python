"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#StartDataIngestionJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.ingestion_job_id
    import aws_sdk_lookoutequipment.types.ingestion_job_status


class StartDataIngestionJobResponse(TypedDict):
    job_id: NotRequired[
        "aws_sdk_lookoutequipment.types.ingestion_job_id.IngestionJobId"
    ]
    """<p>Indicates the job ID of the data ingestion job. </p>"""
    status: NotRequired[
        "aws_sdk_lookoutequipment.types.ingestion_job_status.IngestionJobStatus"
    ]
    """<p>Indicates the status of the <code>StartDataIngestionJob</code> operation. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartDataIngestionJobResponse) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    if "status" in value:
        import aws_sdk_lookoutequipment.types.ingestion_job_status

        out["Status"] = (
            aws_sdk_lookoutequipment.types.ingestion_job_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> StartDataIngestionJobResponse:
    out: StartDataIngestionJobResponse = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    if "Status" in data:
        import aws_sdk_lookoutequipment.types.ingestion_job_status

        out["status"] = (
            aws_sdk_lookoutequipment.types.ingestion_job_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    return out

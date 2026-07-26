"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#StartDataIngestionJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.ingestion_job_id
    import capo_lookoutequipment.types.ingestion_job_status


class StartDataIngestionJobResponse(TypedDict, closed=True):
    job_id: NotRequired["capo_lookoutequipment.types.ingestion_job_id.IngestionJobId"]
    """<p>Indicates the job ID of the data ingestion job. </p>"""
    status: NotRequired[
        "capo_lookoutequipment.types.ingestion_job_status.IngestionJobStatus"
    ]
    """<p>Indicates the status of the <code>StartDataIngestionJob</code> operation. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartDataIngestionJobResponse) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    if "status" in value:
        import capo_lookoutequipment.types.ingestion_job_status

        out["Status"] = (
            capo_lookoutequipment.types.ingestion_job_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> StartDataIngestionJobResponse:
    out: StartDataIngestionJobResponse = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    if "Status" in data:
        import capo_lookoutequipment.types.ingestion_job_status

        out["status"] = (
            capo_lookoutequipment.types.ingestion_job_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    return out

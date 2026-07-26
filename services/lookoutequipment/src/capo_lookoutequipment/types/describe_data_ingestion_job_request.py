"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#DescribeDataIngestionJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lookoutequipment.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lookoutequipment.types.ingestion_job_id


class DescribeDataIngestionJobRequest(TypedDict, closed=True):
    job_id: "capo_lookoutequipment.types.ingestion_job_id.IngestionJobId"
    """<p>The job ID of the data ingestion job. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeDataIngestionJobRequest) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeDataIngestionJobRequest:
    out: DescribeDataIngestionJobRequest = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    else:
        raise DeserializationError("DescribeDataIngestionJobRequest.job_id required")
    return out

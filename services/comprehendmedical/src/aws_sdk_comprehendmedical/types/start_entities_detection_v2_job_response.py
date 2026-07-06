"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#StartEntitiesDetectionV2JobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_comprehendmedical.types.job_id


class StartEntitiesDetectionV2JobResponse(TypedDict, closed=True):
    job_id: NotRequired["aws_sdk_comprehendmedical.types.job_id.JobId"]
    """<p>The identifier generated for the job. To get the status of a job, use this identifier with the <code>DescribeEntitiesDetectionV2Job</code> operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartEntitiesDetectionV2JobResponse) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartEntitiesDetectionV2JobResponse:
    out: StartEntitiesDetectionV2JobResponse = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    return out

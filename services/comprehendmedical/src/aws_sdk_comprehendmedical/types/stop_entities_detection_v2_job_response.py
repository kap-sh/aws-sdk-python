"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#StopEntitiesDetectionV2JobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehendmedical.types.job_id


class StopEntitiesDetectionV2JobResponse(TypedDict):
    job_id: NotRequired["aws_sdk_comprehendmedical.types.job_id.JobId"]
    """<p>The identifier of the medical entities detection job that was stopped.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopEntitiesDetectionV2JobResponse) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopEntitiesDetectionV2JobResponse:
    out: StopEntitiesDetectionV2JobResponse = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    return out

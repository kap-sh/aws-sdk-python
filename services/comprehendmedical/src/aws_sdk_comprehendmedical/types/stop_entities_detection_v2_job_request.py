"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#StopEntitiesDetectionV2JobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_comprehendmedical.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_comprehendmedical.types.job_id


class StopEntitiesDetectionV2JobRequest(TypedDict):
    job_id: "aws_sdk_comprehendmedical.types.job_id.JobId"
    """<p>The identifier of the medical entities job to stop.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopEntitiesDetectionV2JobRequest) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopEntitiesDetectionV2JobRequest:
    out: StopEntitiesDetectionV2JobRequest = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    else:
        raise DeserializationError("StopEntitiesDetectionV2JobRequest.job_id required")
    return out

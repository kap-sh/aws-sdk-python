"""Generated from Smithy shape ``com.amazonaws.location#CancelJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.geo_arn
    import aws_sdk_location.types.job_id
    import aws_sdk_location.types.job_status


class CancelJobResponse(TypedDict):
    job_arn: "aws_sdk_location.types.geo_arn.GeoArn"
    """<p>Amazon Resource Name (ARN) of the cancelled job.</p>"""
    job_id: "aws_sdk_location.types.job_id.JobId"
    """<p>Unique job identifier.</p>"""
    status: "aws_sdk_location.types.job_status.JobStatus"
    """<p>Job status after cancellation request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelJobResponse) -> dict:
    out: dict = {}
    out["JobArn"] = value["job_arn"]
    out["JobId"] = value["job_id"]
    out["Status"] = value["status"]
    return out


def deserialize_json(data: dict) -> CancelJobResponse:
    out: CancelJobResponse = {}  # type: ignore[typeddict-item]
    if "JobArn" in data:
        out["job_arn"] = data["JobArn"]
    else:
        raise DeserializationError("CancelJobResponse.job_arn required")
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    else:
        raise DeserializationError("CancelJobResponse.job_id required")
    if "Status" in data:
        out["status"] = data["Status"]
    else:
        raise DeserializationError("CancelJobResponse.status required")
    return out

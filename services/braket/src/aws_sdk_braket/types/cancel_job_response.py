"""Generated from Smithy shape ``com.amazonaws.braket#CancelJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_braket.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_braket.types.cancellation_status
    import aws_sdk_braket.types.job_arn


class CancelJobResponse(TypedDict):
    job_arn: "aws_sdk_braket.types.job_arn.JobArn"
    """<p>The ARN of the Amazon Braket job.</p>"""
    cancellation_status: "aws_sdk_braket.types.cancellation_status.CancellationStatus"
    """<p>The status of the hybrid job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelJobResponse) -> dict:
    out: dict = {}
    out["jobArn"] = value["job_arn"]
    out["cancellationStatus"] = value["cancellation_status"]
    return out


def deserialize_json(data: dict) -> CancelJobResponse:
    out: CancelJobResponse = {}  # type: ignore[typeddict-item]
    if "jobArn" in data:
        out["job_arn"] = data["jobArn"]
    else:
        raise DeserializationError("CancelJobResponse.job_arn required")
    if "cancellationStatus" in data:
        out["cancellation_status"] = data["cancellationStatus"]
    else:
        raise DeserializationError("CancelJobResponse.cancellation_status required")
    return out

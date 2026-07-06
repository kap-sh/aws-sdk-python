"""Generated from Smithy shape ``com.amazonaws.batch#TerminateServiceJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_batch.types.string


class TerminateServiceJobRequest(TypedDict, closed=True):
    job_id: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The service job ID of the service job to terminate.</p>"""
    reason: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>A message to attach to the service job that explains the reason for canceling it. This message is returned by <code>DescribeServiceJob</code> operations on the service job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TerminateServiceJobRequest) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    if "reason" in value:
        out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> TerminateServiceJobRequest:
    out: TerminateServiceJobRequest = {}  # type: ignore[typeddict-item]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    if "reason" in data:
        out["reason"] = data["reason"]
    return out

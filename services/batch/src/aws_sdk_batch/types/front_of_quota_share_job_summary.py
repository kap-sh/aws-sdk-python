"""Generated from Smithy shape ``com.amazonaws.batch#FrontOfQuotaShareJobSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.long
    import aws_sdk_batch.types.string


class FrontOfQuotaShareJobSummary(TypedDict):
    job_arn: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The ARN for a job in a named quota share.</p>"""
    earliest_time_at_position: NotRequired["aws_sdk_batch.types.long.Long"]
    """<p>The Unix timestamp (in milliseconds) for when the job transitioned to its current position in the quota share.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FrontOfQuotaShareJobSummary) -> dict:
    out: dict = {}
    if "job_arn" in value:
        out["jobArn"] = value["job_arn"]
    if "earliest_time_at_position" in value:
        out["earliestTimeAtPosition"] = value["earliest_time_at_position"]
    return out


def deserialize_json(data: dict) -> FrontOfQuotaShareJobSummary:
    out: FrontOfQuotaShareJobSummary = {}  # type: ignore[typeddict-item]
    if "jobArn" in data:
        out["job_arn"] = data["jobArn"]
    if "earliestTimeAtPosition" in data:
        out["earliest_time_at_position"] = data["earliestTimeAtPosition"]
    return out

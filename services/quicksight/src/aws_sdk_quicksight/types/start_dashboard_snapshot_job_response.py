"""Generated from Smithy shape ``com.amazonaws.quicksight#StartDashboardSnapshotJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.non_empty_string
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.status_code


class StartDashboardSnapshotJobResponse(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) for the dashboard snapshot job.</p>"""
    snapshot_job_id: NotRequired[
        "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>The ID of the job. The job ID is set when you start a new job with a <code>StartDashboardSnapshotJob</code> API call.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.non_empty_string.NonEmptyString"]
    """<p> The Amazon Web Services request ID for this operation. </p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartDashboardSnapshotJobResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "snapshot_job_id" in value:
        out["SnapshotJobId"] = value["snapshot_job_id"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> StartDashboardSnapshotJobResponse:
    out: StartDashboardSnapshotJobResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "SnapshotJobId" in data:
        out["snapshot_job_id"] = data["SnapshotJobId"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out

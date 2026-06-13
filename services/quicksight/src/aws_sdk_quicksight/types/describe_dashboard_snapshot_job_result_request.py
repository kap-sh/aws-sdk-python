"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeDashboardSnapshotJobResultRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.short_restrictive_resource_id


class DescribeDashboardSnapshotJobResultRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that the dashboard snapshot job is executed in.</p>"""
    dashboard_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The ID of the dashboard that you have started a snapshot job for.</p>"""
    snapshot_job_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The ID of the job to be described. The job ID is set when you start a new job with a <code>StartDashboardSnapshotJob</code> API call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDashboardSnapshotJobResultRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeDashboardSnapshotJobResultRequest:
    out: DescribeDashboardSnapshotJobResultRequest = {}  # type: ignore[typeddict-item]
    return out

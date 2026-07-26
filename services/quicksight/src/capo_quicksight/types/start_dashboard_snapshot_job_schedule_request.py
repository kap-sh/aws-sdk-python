"""Generated from Smithy shape ``com.amazonaws.quicksight#StartDashboardSnapshotJobScheduleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.short_restrictive_resource_id


class StartDashboardSnapshotJobScheduleRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that the dashboard snapshot job is executed in.</p>"""
    dashboard_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The ID of the dashboard that you want to start a snapshot job schedule for. </p>"""
    schedule_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The ID of the schedule that you want to start a snapshot job schedule for. The schedule ID can be found in the Amazon Quick Sight console in the <b>Schedules</b> pane of the dashboard that the schedule is configured for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartDashboardSnapshotJobScheduleRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StartDashboardSnapshotJobScheduleRequest:
    out: StartDashboardSnapshotJobScheduleRequest = {}  # type: ignore[typeddict-item]
    return out

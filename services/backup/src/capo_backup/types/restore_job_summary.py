"""Generated from Smithy shape ``com.amazonaws.backup#RestoreJobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.account_id
    import capo_backup.types.integer
    import capo_backup.types.region
    import capo_backup.types.resource_type
    import capo_backup.types.restore_job_state
    import capo_backup.types.timestamp


class RestoreJobSummary(TypedDict, closed=True):
    region: NotRequired["capo_backup.types.region.Region"]
    """<p>The Amazon Web Services Regions within the job summary.</p>"""
    account_id: NotRequired["capo_backup.types.account_id.AccountId"]
    """<p>The account ID that owns the jobs within the summary.</p>"""
    state: NotRequired["capo_backup.types.restore_job_state.RestoreJobState"]
    """<p>This value is job count for jobs with the specified state.</p>"""
    resource_type: NotRequired["capo_backup.types.resource_type.ResourceType"]
    """<p>This value is the job count for the specified resource type. The request <code>GetSupportedResourceTypes</code> returns strings for supported resource types.</p>"""
    count: "capo_backup.types.integer.integer"
    """<p>The value as a number of jobs in a job summary.</p>"""
    start_time: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>The value of time in number format of a job start time.</p> <p>This value is the time in Unix format, Coordinated Universal Time (UTC), and accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    end_time: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>The value of time in number format of a job end time.</p> <p>This value is the time in Unix format, Coordinated Universal Time (UTC), and accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RestoreJobSummary) -> dict:
    out: dict = {}
    if "region" in value:
        out["Region"] = value["region"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "state" in value:
        import capo_backup.types.restore_job_state

        out["State"] = capo_backup.types.restore_job_state.serialize_json(
            value["state"]
        )
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    out["Count"] = value.get("count", 0)
    if "start_time" in value:
        import capo_backup.types.timestamp

        out["StartTime"] = capo_backup.types.timestamp.serialize_json(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_backup.types.timestamp

        out["EndTime"] = capo_backup.types.timestamp.serialize_json(value["end_time"])
    return out


def deserialize_json(data: dict) -> RestoreJobSummary:
    out: RestoreJobSummary = {}  # type: ignore[typeddict-item]
    if "Region" in data:
        out["region"] = data["Region"]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "State" in data:
        import capo_backup.types.restore_job_state

        out["state"] = capo_backup.types.restore_job_state.deserialize_json(
            data["State"]
        )
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    if "Count" in data:
        out["count"] = data["Count"]
    else:
        out["count"] = 0
    if "StartTime" in data:
        import capo_backup.types.timestamp

        out["start_time"] = capo_backup.types.timestamp.deserialize_json(
            data["StartTime"]
        )
    if "EndTime" in data:
        import capo_backup.types.timestamp

        out["end_time"] = capo_backup.types.timestamp.deserialize_json(data["EndTime"])
    return out

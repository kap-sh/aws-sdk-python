"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#SyncJobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.id
    import capo_iottwinmaker.types.sync_job_status
    import capo_iottwinmaker.types.sync_source
    import capo_iottwinmaker.types.timestamp
    import capo_iottwinmaker.types.twin_maker_arn


class SyncJobSummary(TypedDict, closed=True):
    arn: NotRequired["capo_iottwinmaker.types.twin_maker_arn.TwinMakerArn"]
    """<p>The SyncJob summary ARN.</p>"""
    workspace_id: NotRequired["capo_iottwinmaker.types.id.Id"]
    """<p>The ID of the workspace that contains the sync job.</p>"""
    sync_source: NotRequired["capo_iottwinmaker.types.sync_source.SyncSource"]
    """<p>The sync source.</p>"""
    status: NotRequired["capo_iottwinmaker.types.sync_job_status.SyncJobStatus"]
    """<p>The SyncJob summaries status.</p>"""
    creation_date_time: NotRequired["capo_iottwinmaker.types.timestamp.Timestamp"]
    """<p>The creation date and time.</p>"""
    update_date_time: NotRequired["capo_iottwinmaker.types.timestamp.Timestamp"]
    """<p>The update date and time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SyncJobSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "workspace_id" in value:
        out["workspaceId"] = value["workspace_id"]
    if "sync_source" in value:
        out["syncSource"] = value["sync_source"]
    if "status" in value:
        import capo_iottwinmaker.types.sync_job_status

        out["status"] = capo_iottwinmaker.types.sync_job_status.serialize_json(
            value["status"]
        )
    if "creation_date_time" in value:
        import capo_iottwinmaker.types.timestamp

        out["creationDateTime"] = capo_iottwinmaker.types.timestamp.serialize_json(
            value["creation_date_time"]
        )
    if "update_date_time" in value:
        import capo_iottwinmaker.types.timestamp

        out["updateDateTime"] = capo_iottwinmaker.types.timestamp.serialize_json(
            value["update_date_time"]
        )
    return out


def deserialize_json(data: dict) -> SyncJobSummary:
    out: SyncJobSummary = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "workspaceId" in data:
        out["workspace_id"] = data["workspaceId"]
    if "syncSource" in data:
        out["sync_source"] = data["syncSource"]
    if "status" in data:
        import capo_iottwinmaker.types.sync_job_status

        out["status"] = capo_iottwinmaker.types.sync_job_status.deserialize_json(
            data["status"]
        )
    if "creationDateTime" in data:
        import capo_iottwinmaker.types.timestamp

        out["creation_date_time"] = capo_iottwinmaker.types.timestamp.deserialize_json(
            data["creationDateTime"]
        )
    if "updateDateTime" in data:
        import capo_iottwinmaker.types.timestamp

        out["update_date_time"] = capo_iottwinmaker.types.timestamp.deserialize_json(
            data["updateDateTime"]
        )
    return out

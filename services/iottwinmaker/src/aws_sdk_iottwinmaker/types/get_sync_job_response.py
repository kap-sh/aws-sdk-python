"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#GetSyncJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.id
    import aws_sdk_iottwinmaker.types.role_arn
    import aws_sdk_iottwinmaker.types.sync_job_status
    import aws_sdk_iottwinmaker.types.sync_source
    import aws_sdk_iottwinmaker.types.timestamp
    import aws_sdk_iottwinmaker.types.twin_maker_arn


class GetSyncJobResponse(TypedDict):
    arn: "aws_sdk_iottwinmaker.types.twin_maker_arn.TwinMakerArn"
    """<p>The sync job ARN.</p>"""
    workspace_id: "aws_sdk_iottwinmaker.types.id.Id"
    """<p>The ID of the workspace that contains the sync job.</p>"""
    sync_source: "aws_sdk_iottwinmaker.types.sync_source.SyncSource"
    """<p>The sync soucre.</p> <note> <p>Currently the only supported syncSource is <code>SITEWISE </code>.</p> </note>"""
    sync_role: "aws_sdk_iottwinmaker.types.role_arn.RoleArn"
    """<p>The sync IAM role.</p>"""
    status: "aws_sdk_iottwinmaker.types.sync_job_status.SyncJobStatus"
    """<p>The SyncJob response status.</p>"""
    creation_date_time: "aws_sdk_iottwinmaker.types.timestamp.Timestamp"
    """<p>The creation date and time.</p>"""
    update_date_time: "aws_sdk_iottwinmaker.types.timestamp.Timestamp"
    """<p>The update date and time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSyncJobResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["workspaceId"] = value["workspace_id"]
    out["syncSource"] = value["sync_source"]
    out["syncRole"] = value["sync_role"]
    import aws_sdk_iottwinmaker.types.sync_job_status

    out["status"] = aws_sdk_iottwinmaker.types.sync_job_status.serialize_json(
        value["status"]
    )
    import aws_sdk_iottwinmaker.types.timestamp

    out["creationDateTime"] = aws_sdk_iottwinmaker.types.timestamp.serialize_json(
        value["creation_date_time"]
    )
    import aws_sdk_iottwinmaker.types.timestamp

    out["updateDateTime"] = aws_sdk_iottwinmaker.types.timestamp.serialize_json(
        value["update_date_time"]
    )
    return out


def deserialize_json(data: dict) -> GetSyncJobResponse:
    out: GetSyncJobResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("GetSyncJobResponse.arn required")
    if "workspaceId" in data:
        out["workspace_id"] = data["workspaceId"]
    else:
        raise DeserializationError("GetSyncJobResponse.workspace_id required")
    if "syncSource" in data:
        out["sync_source"] = data["syncSource"]
    else:
        raise DeserializationError("GetSyncJobResponse.sync_source required")
    if "syncRole" in data:
        out["sync_role"] = data["syncRole"]
    else:
        raise DeserializationError("GetSyncJobResponse.sync_role required")
    if "status" in data:
        import aws_sdk_iottwinmaker.types.sync_job_status

        out["status"] = aws_sdk_iottwinmaker.types.sync_job_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("GetSyncJobResponse.status required")
    if "creationDateTime" in data:
        import aws_sdk_iottwinmaker.types.timestamp

        out["creation_date_time"] = (
            aws_sdk_iottwinmaker.types.timestamp.deserialize_json(
                data["creationDateTime"]
            )
        )
    else:
        raise DeserializationError("GetSyncJobResponse.creation_date_time required")
    if "updateDateTime" in data:
        import aws_sdk_iottwinmaker.types.timestamp

        out["update_date_time"] = aws_sdk_iottwinmaker.types.timestamp.deserialize_json(
            data["updateDateTime"]
        )
    else:
        raise DeserializationError("GetSyncJobResponse.update_date_time required")
    return out

"""Generated from Smithy shape ``com.amazonaws.backup#CreateBackupPlanInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_backup.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_backup.types.backup_plan_input
    import aws_sdk_backup.types.string
    import aws_sdk_backup.types.tags


class CreateBackupPlanInput(TypedDict):
    backup_plan: "aws_sdk_backup.types.backup_plan_input.BackupPlanInput"
    """<p>The body of a backup plan. Includes a <code>BackupPlanName</code> and one or more sets of <code>Rules</code>.</p>"""
    backup_plan_tags: NotRequired["aws_sdk_backup.types.tags.Tags"]
    """<p>The tags to assign to the backup plan.</p>"""
    creator_request_id: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>Identifies the request and allows failed requests to be retried without the risk of running the operation twice. If the request includes a <code>CreatorRequestId</code> that matches an existing backup plan, that plan is returned. This parameter is optional.</p> <p>If used, this parameter must contain 1 to 50 alphanumeric or '-_.' characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBackupPlanInput) -> dict:
    out: dict = {}
    import aws_sdk_backup.types.backup_plan_input

    out["BackupPlan"] = aws_sdk_backup.types.backup_plan_input.serialize_json(
        value["backup_plan"]
    )
    if "backup_plan_tags" in value:
        import aws_sdk_backup.types.tags

        out["BackupPlanTags"] = aws_sdk_backup.types.tags.serialize_json(
            value["backup_plan_tags"]
        )
    if "creator_request_id" in value:
        out["CreatorRequestId"] = value["creator_request_id"]
    return out


def deserialize_json(data: dict) -> CreateBackupPlanInput:
    out: CreateBackupPlanInput = {}  # type: ignore[typeddict-item]
    if "BackupPlan" in data:
        import aws_sdk_backup.types.backup_plan_input

        out["backup_plan"] = aws_sdk_backup.types.backup_plan_input.deserialize_json(
            data["BackupPlan"]
        )
    else:
        raise DeserializationError("CreateBackupPlanInput.backup_plan required")
    if "BackupPlanTags" in data:
        import aws_sdk_backup.types.tags

        out["backup_plan_tags"] = aws_sdk_backup.types.tags.deserialize_json(
            data["BackupPlanTags"]
        )
    if "CreatorRequestId" in data:
        out["creator_request_id"] = data["CreatorRequestId"]
    return out

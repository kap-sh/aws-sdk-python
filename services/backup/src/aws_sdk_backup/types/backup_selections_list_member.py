"""Generated from Smithy shape ``com.amazonaws.backup#BackupSelectionsListMember``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_backup.types.backup_selection_name
    import aws_sdk_backup.types.iam_role_arn
    import aws_sdk_backup.types.string
    import aws_sdk_backup.types.timestamp


class BackupSelectionsListMember(TypedDict, closed=True):
    selection_id: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>Uniquely identifies a request to assign a set of resources to a backup plan.</p>"""
    selection_name: NotRequired[
        "aws_sdk_backup.types.backup_selection_name.BackupSelectionName"
    ]
    """<p>The display name of a resource selection document.</p>"""
    backup_plan_id: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>Uniquely identifies a backup plan.</p>"""
    creation_date: NotRequired["aws_sdk_backup.types.timestamp.timestamp"]
    """<p>The date and time a backup plan is created, in Unix format and Coordinated Universal Time (UTC). The value of <code>CreationDate</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    creator_request_id: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>A unique string that identifies the request and allows failed requests to be retried without the risk of running the operation twice. This parameter is optional.</p> <p>If used, this parameter must contain 1 to 50 alphanumeric or '-_.' characters.</p>"""
    iam_role_arn: NotRequired["aws_sdk_backup.types.iam_role_arn.IAMRoleArn"]
    """<p>Specifies the IAM role Amazon Resource Name (ARN) to create the target recovery point; for example, <code>arn:aws:iam::123456789012:role/S3Access</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BackupSelectionsListMember) -> dict:
    out: dict = {}
    if "selection_id" in value:
        out["SelectionId"] = value["selection_id"]
    if "selection_name" in value:
        out["SelectionName"] = value["selection_name"]
    if "backup_plan_id" in value:
        out["BackupPlanId"] = value["backup_plan_id"]
    if "creation_date" in value:
        import aws_sdk_backup.types.timestamp

        out["CreationDate"] = aws_sdk_backup.types.timestamp.serialize_json(
            value["creation_date"]
        )
    if "creator_request_id" in value:
        out["CreatorRequestId"] = value["creator_request_id"]
    if "iam_role_arn" in value:
        out["IamRoleArn"] = value["iam_role_arn"]
    return out


def deserialize_json(data: dict) -> BackupSelectionsListMember:
    out: BackupSelectionsListMember = {}  # type: ignore[typeddict-item]
    if "SelectionId" in data:
        out["selection_id"] = data["SelectionId"]
    if "SelectionName" in data:
        out["selection_name"] = data["SelectionName"]
    if "BackupPlanId" in data:
        out["backup_plan_id"] = data["BackupPlanId"]
    if "CreationDate" in data:
        import aws_sdk_backup.types.timestamp

        out["creation_date"] = aws_sdk_backup.types.timestamp.deserialize_json(
            data["CreationDate"]
        )
    if "CreatorRequestId" in data:
        out["creator_request_id"] = data["CreatorRequestId"]
    if "IamRoleArn" in data:
        out["iam_role_arn"] = data["IamRoleArn"]
    return out

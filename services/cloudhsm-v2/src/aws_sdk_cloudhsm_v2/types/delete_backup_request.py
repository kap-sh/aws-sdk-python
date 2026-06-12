"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#DeleteBackupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudhsm_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudhsm_v2.types.backup_id


class DeleteBackupRequest(TypedDict):
    backup_id: "aws_sdk_cloudhsm_v2.types.backup_id.BackupId"
    """<p>The ID of the backup to be deleted. To find the ID of a backup, use the <a>DescribeBackups</a> operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteBackupRequest) -> dict:
    out: dict = {}
    out["BackupId"] = value["backup_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteBackupRequest:
    out: DeleteBackupRequest = {}  # type: ignore[typeddict-item]
    if "BackupId" in data:
        out["backup_id"] = data["BackupId"]
    else:
        raise DeserializationError("DeleteBackupRequest.backup_id required")
    return out

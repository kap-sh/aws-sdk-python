"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#RestoreBackupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudhsm_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudhsm_v2.types.backup_id


class RestoreBackupRequest(TypedDict, closed=True):
    backup_id: "aws_sdk_cloudhsm_v2.types.backup_id.BackupId"
    """<p>The ID of the backup to be restored. To find the ID of a backup, use the <a>DescribeBackups</a> operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RestoreBackupRequest) -> dict:
    out: dict = {}
    out["BackupId"] = value["backup_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RestoreBackupRequest:
    out: RestoreBackupRequest = {}  # type: ignore[typeddict-item]
    if "BackupId" in data:
        out["backup_id"] = data["BackupId"]
    else:
        raise DeserializationError("RestoreBackupRequest.backup_id required")
    return out

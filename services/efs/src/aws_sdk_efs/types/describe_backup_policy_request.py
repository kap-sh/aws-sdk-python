"""Generated from Smithy shape ``com.amazonaws.efs#DescribeBackupPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_efs.types.file_system_id


class DescribeBackupPolicyRequest(TypedDict, closed=True):
    file_system_id: "aws_sdk_efs.types.file_system_id.FileSystemId"
    """<p>Specifies which EFS file system for which to retrieve the <code>BackupPolicy</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeBackupPolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeBackupPolicyRequest:
    out: DescribeBackupPolicyRequest = {}  # type: ignore[typeddict-item]
    return out

"""Generated from Smithy shape ``com.amazonaws.efs#FileSystemPolicyDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_efs.types.file_system_id
    import aws_sdk_efs.types.policy


class FileSystemPolicyDescription(TypedDict, closed=True):
    file_system_id: NotRequired["aws_sdk_efs.types.file_system_id.FileSystemId"]
    """<p>Specifies the EFS file system to which the <code>FileSystemPolicy</code> applies.</p>"""
    policy: NotRequired["aws_sdk_efs.types.policy.Policy"]
    """<p>The JSON formatted <code>FileSystemPolicy</code> for the EFS file system.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FileSystemPolicyDescription) -> dict:
    out: dict = {}
    if "file_system_id" in value:
        out["FileSystemId"] = value["file_system_id"]
    if "policy" in value:
        out["Policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> FileSystemPolicyDescription:
    out: FileSystemPolicyDescription = {}  # type: ignore[typeddict-item]
    if "FileSystemId" in data:
        out["file_system_id"] = data["FileSystemId"]
    if "Policy" in data:
        out["policy"] = data["Policy"]
    return out

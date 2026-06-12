"""Generated from Smithy shape ``com.amazonaws.efs#DeleteFileSystemPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_efs.types.file_system_id


class DeleteFileSystemPolicyRequest(TypedDict):
    file_system_id: "aws_sdk_efs.types.file_system_id.FileSystemId"
    """<p>Specifies the EFS file system for which to delete the <code>FileSystemPolicy</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFileSystemPolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteFileSystemPolicyRequest:
    out: DeleteFileSystemPolicyRequest = {}  # type: ignore[typeddict-item]
    return out

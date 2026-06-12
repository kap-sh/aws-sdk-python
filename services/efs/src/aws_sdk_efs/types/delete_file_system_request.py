"""Generated from Smithy shape ``com.amazonaws.efs#DeleteFileSystemRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_efs.types.file_system_id


class DeleteFileSystemRequest(TypedDict):
    file_system_id: "aws_sdk_efs.types.file_system_id.FileSystemId"
    """<p>The ID of the file system you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFileSystemRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteFileSystemRequest:
    out: DeleteFileSystemRequest = {}  # type: ignore[typeddict-item]
    return out

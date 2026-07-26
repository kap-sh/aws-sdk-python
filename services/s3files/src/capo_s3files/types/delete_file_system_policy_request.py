"""Generated from Smithy shape ``com.amazonaws.s3files#DeleteFileSystemPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_s3files.types.file_system_id


class DeleteFileSystemPolicyRequest(TypedDict, closed=True):
    file_system_id: "capo_s3files.types.file_system_id.FileSystemId"
    """<p>The ID or Amazon Resource Name (ARN) of the S3 File System whose resource policy to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFileSystemPolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteFileSystemPolicyRequest:
    out: DeleteFileSystemPolicyRequest = {}  # type: ignore[typeddict-item]
    return out

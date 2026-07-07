"""Generated from Smithy shape ``com.amazonaws.s3files#DeleteFileSystemRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_s3files.types.file_system_id


class DeleteFileSystemRequest(TypedDict, closed=True):
    file_system_id: "aws_sdk_s3files.types.file_system_id.FileSystemId"
    """<p>The ID or Amazon Resource Name (ARN) of the S3 File System to delete.</p>"""
    force_delete: NotRequired["bool"]
    """<p>If true, allows deletion of a file system that contains data pending export to S3. If false (the default), the deletion will fail if there is data that has not yet been exported to the S3 bucket. Use this parameter with caution as it may result in data loss.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFileSystemRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteFileSystemRequest:
    out: DeleteFileSystemRequest = {}  # type: ignore[typeddict-item]
    return out

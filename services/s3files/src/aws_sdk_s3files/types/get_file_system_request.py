"""Generated from Smithy shape ``com.amazonaws.s3files#GetFileSystemRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_s3files.types.file_system_id


class GetFileSystemRequest(TypedDict):
    file_system_id: "aws_sdk_s3files.types.file_system_id.FileSystemId"
    """<p>The ID or Amazon Resource Name (ARN) of the S3 File System to retrieve information for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFileSystemRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetFileSystemRequest:
    out: GetFileSystemRequest = {}  # type: ignore[typeddict-item]
    return out

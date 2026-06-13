"""Generated from Smithy shape ``com.amazonaws.s3files#ListAccessPointsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_s3files.types.file_system_id


class ListAccessPointsRequest(TypedDict):
    file_system_id: "aws_sdk_s3files.types.file_system_id.FileSystemId"
    """<p>The ID or Amazon Resource Name (ARN) of the S3 File System to list access points for.</p>"""
    max_results: "int"
    """<p>The maximum number of access points to return in a single response.</p>"""
    next_token: NotRequired["str"]
    """<p>A pagination token returned from a previous call to continue listing access points.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAccessPointsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAccessPointsRequest:
    out: ListAccessPointsRequest = {}  # type: ignore[typeddict-item]
    return out

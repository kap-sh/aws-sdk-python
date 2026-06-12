"""Generated from Smithy shape ``com.amazonaws.storagegateway#FileSystemAssociationStatusDetail``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.file_system_association_sync_error_code


class FileSystemAssociationStatusDetail(TypedDict):
    error_code: NotRequired[
        "aws_sdk_storage_gateway.types.file_system_association_sync_error_code.FileSystemAssociationSyncErrorCode"
    ]
    """<p>The error code for a given file system association status.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileSystemAssociationStatusDetail) -> dict:
    out: dict = {}
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FileSystemAssociationStatusDetail:
    out: FileSystemAssociationStatusDetail = {}  # type: ignore[typeddict-item]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    return out

"""Generated from Smithy shape ``com.amazonaws.efs#FileSystemAlreadyExists``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_efs.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_efs.types.error_code
    import aws_sdk_efs.types.error_message
    import aws_sdk_efs.types.file_system_id


class FileSystemAlreadyExists_(TypedDict, closed=True):
    error_code: "aws_sdk_efs.types.error_code.ErrorCode"
    message: NotRequired["aws_sdk_efs.types.error_message.ErrorMessage"]
    file_system_id: "aws_sdk_efs.types.file_system_id.FileSystemId"


# --- restJson1 ser/de ---
def serialize_json(value: FileSystemAlreadyExists_) -> dict:
    out: dict = {}
    out["ErrorCode"] = value["error_code"]
    if "message" in value:
        out["Message"] = value["message"]
    out["FileSystemId"] = value["file_system_id"]
    return out


def deserialize_json(data: dict) -> FileSystemAlreadyExists_:
    out: FileSystemAlreadyExists_ = {}  # type: ignore[typeddict-item]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    else:
        raise DeserializationError("FileSystemAlreadyExists_.error_code required")
    if "Message" in data:
        out["message"] = data["Message"]
    if "FileSystemId" in data:
        out["file_system_id"] = data["FileSystemId"]
    else:
        raise DeserializationError("FileSystemAlreadyExists_.file_system_id required")
    return out


class FileSystemAlreadyExists(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.efs#FileSystemAlreadyExists``."""

    code: str | None = "FileSystemAlreadyExists"

    def __init__(self, data: FileSystemAlreadyExists_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="FileSystemAlreadyExists",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "FileSystemAlreadyExists":
        return cls(deserialize_json(data))

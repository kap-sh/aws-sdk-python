"""Generated from Smithy shape ``com.amazonaws.efs#FileSystemNotFound``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_efs.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_efs.types.error_code
    import aws_sdk_efs.types.error_message


class FileSystemNotFound_(TypedDict, closed=True):
    error_code: "aws_sdk_efs.types.error_code.ErrorCode"
    message: NotRequired["aws_sdk_efs.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: FileSystemNotFound_) -> dict:
    out: dict = {}
    out["ErrorCode"] = value["error_code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> FileSystemNotFound_:
    out: FileSystemNotFound_ = {}  # type: ignore[typeddict-item]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    else:
        raise DeserializationError("FileSystemNotFound_.error_code required")
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class FileSystemNotFound(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.efs#FileSystemNotFound``."""

    code: str | None = "FileSystemNotFound"

    def __init__(self, data: FileSystemNotFound_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="FileSystemNotFound",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "FileSystemNotFound":
        return cls(deserialize_json(data))

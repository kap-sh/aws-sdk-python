"""Generated from Smithy shape ``com.amazonaws.efs#FileSystemInUse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_efs.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_efs.types.error_code
    import capo_efs.types.error_message


class FileSystemInUse_(TypedDict, closed=True):
    error_code: "capo_efs.types.error_code.ErrorCode"
    message: NotRequired["capo_efs.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: FileSystemInUse_) -> dict:
    out: dict = {}
    out["ErrorCode"] = value["error_code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> FileSystemInUse_:
    out: FileSystemInUse_ = {}  # type: ignore[typeddict-item]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    else:
        raise DeserializationError("FileSystemInUse_.error_code required")
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class FileSystemInUse(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.efs#FileSystemInUse``."""

    code: str | None = "FileSystemInUse"

    def __init__(self, data: FileSystemInUse_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="FileSystemInUse",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "FileSystemInUse":
        return cls(deserialize_json(data))

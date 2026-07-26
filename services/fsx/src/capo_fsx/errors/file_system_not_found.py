"""Generated from Smithy shape ``com.amazonaws.fsx#FileSystemNotFound``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_fsx.errors import ServiceError

if TYPE_CHECKING:
    import capo_fsx.types.error_message


class FileSystemNotFound_(TypedDict, closed=True):
    message: NotRequired["capo_fsx.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileSystemNotFound_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FileSystemNotFound_:
    out: FileSystemNotFound_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class FileSystemNotFound(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.fsx#FileSystemNotFound``."""

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
    def from_aws_json_1_1(cls, data: dict) -> "FileSystemNotFound":
        return cls(deserialize_aws_json_1_1(data))

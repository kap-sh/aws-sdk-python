"""Generated from Smithy shape ``com.amazonaws.directoryservice#DirectoryInDesiredStateException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_directory_service.errors import ServiceError

if TYPE_CHECKING:
    import capo_directory_service.types.exception_message
    import capo_directory_service.types.request_id


class DirectoryInDesiredStateException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_directory_service.types.exception_message.ExceptionMessage"
    ]
    request_id: NotRequired["capo_directory_service.types.request_id.RequestId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DirectoryInDesiredStateException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DirectoryInDesiredStateException_:
    out: DirectoryInDesiredStateException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out


class DirectoryInDesiredStateException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.directoryservice#DirectoryInDesiredStateException``."""

    code: str | None = "DirectoryInDesiredStateException"

    def __init__(self, data: DirectoryInDesiredStateException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DirectoryInDesiredStateException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "DirectoryInDesiredStateException":
        return cls(deserialize_aws_json_1_1(data))

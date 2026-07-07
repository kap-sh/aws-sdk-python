"""Generated from Smithy shape ``com.amazonaws.directoryservice#DirectoryDoesNotExistException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_directory_service.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.exception_message
    import aws_sdk_directory_service.types.request_id


class DirectoryDoesNotExistException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_directory_service.types.exception_message.ExceptionMessage"
    ]
    request_id: NotRequired["aws_sdk_directory_service.types.request_id.RequestId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DirectoryDoesNotExistException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DirectoryDoesNotExistException_:
    out: DirectoryDoesNotExistException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out


class DirectoryDoesNotExistException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.directoryservice#DirectoryDoesNotExistException``."""

    code: str | None = "DirectoryDoesNotExistException"

    def __init__(self, data: DirectoryDoesNotExistException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DirectoryDoesNotExistException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "DirectoryDoesNotExistException":
        return cls(deserialize_aws_json_1_1(data))

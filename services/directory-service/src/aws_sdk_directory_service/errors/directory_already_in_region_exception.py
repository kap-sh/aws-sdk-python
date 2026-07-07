"""Generated from Smithy shape ``com.amazonaws.directoryservice#DirectoryAlreadyInRegionException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_directory_service.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.exception_message
    import aws_sdk_directory_service.types.request_id


class DirectoryAlreadyInRegionException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_directory_service.types.exception_message.ExceptionMessage"
    ]
    request_id: NotRequired["aws_sdk_directory_service.types.request_id.RequestId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DirectoryAlreadyInRegionException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DirectoryAlreadyInRegionException_:
    out: DirectoryAlreadyInRegionException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out


class DirectoryAlreadyInRegionException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.directoryservice#DirectoryAlreadyInRegionException``."""

    code: str | None = "DirectoryAlreadyInRegionException"

    def __init__(self, data: DirectoryAlreadyInRegionException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DirectoryAlreadyInRegionException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "DirectoryAlreadyInRegionException":
        return cls(deserialize_aws_json_1_1(data))

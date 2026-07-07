"""Generated from Smithy shape ``com.amazonaws.directoryservice#DisableAlreadyInProgressException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_directory_service.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.exception_message
    import aws_sdk_directory_service.types.request_id


class DisableAlreadyInProgressException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_directory_service.types.exception_message.ExceptionMessage"
    ]
    request_id: NotRequired["aws_sdk_directory_service.types.request_id.RequestId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisableAlreadyInProgressException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DisableAlreadyInProgressException_:
    out: DisableAlreadyInProgressException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out


class DisableAlreadyInProgressException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.directoryservice#DisableAlreadyInProgressException``."""

    code: str | None = "DisableAlreadyInProgressException"

    def __init__(self, data: DisableAlreadyInProgressException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DisableAlreadyInProgressException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "DisableAlreadyInProgressException":
        return cls(deserialize_aws_json_1_1(data))

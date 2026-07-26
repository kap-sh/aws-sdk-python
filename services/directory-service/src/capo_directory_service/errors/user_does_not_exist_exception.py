"""Generated from Smithy shape ``com.amazonaws.directoryservice#UserDoesNotExistException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_directory_service.errors import ServiceError

if TYPE_CHECKING:
    import capo_directory_service.types.exception_message
    import capo_directory_service.types.request_id


class UserDoesNotExistException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_directory_service.types.exception_message.ExceptionMessage"
    ]
    request_id: NotRequired["capo_directory_service.types.request_id.RequestId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserDoesNotExistException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UserDoesNotExistException_:
    out: UserDoesNotExistException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out


class UserDoesNotExistException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.directoryservice#UserDoesNotExistException``."""

    code: str | None = "UserDoesNotExistException"

    def __init__(self, data: UserDoesNotExistException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UserDoesNotExistException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "UserDoesNotExistException":
        return cls(deserialize_aws_json_1_1(data))

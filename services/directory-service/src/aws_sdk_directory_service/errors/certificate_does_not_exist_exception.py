"""Generated from Smithy shape ``com.amazonaws.directoryservice#CertificateDoesNotExistException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_directory_service.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.exception_message
    import aws_sdk_directory_service.types.request_id


class CertificateDoesNotExistException_(TypedDict):
    message: NotRequired[
        "aws_sdk_directory_service.types.exception_message.ExceptionMessage"
    ]
    request_id: NotRequired["aws_sdk_directory_service.types.request_id.RequestId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateDoesNotExistException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CertificateDoesNotExistException_:
    out: CertificateDoesNotExistException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out


class CertificateDoesNotExistException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.directoryservice#CertificateDoesNotExistException``."""

    code: str | None = "CertificateDoesNotExistException"

    def __init__(self, data: CertificateDoesNotExistException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CertificateDoesNotExistException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "CertificateDoesNotExistException":
        return cls(deserialize_aws_json_1_1(data))

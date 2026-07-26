"""Generated from Smithy shape ``com.amazonaws.directoryservice#CertificateAlreadyExistsException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_directory_service.errors import ServiceError

if TYPE_CHECKING:
    import capo_directory_service.types.exception_message
    import capo_directory_service.types.request_id


class CertificateAlreadyExistsException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_directory_service.types.exception_message.ExceptionMessage"
    ]
    request_id: NotRequired["capo_directory_service.types.request_id.RequestId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateAlreadyExistsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CertificateAlreadyExistsException_:
    out: CertificateAlreadyExistsException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out


class CertificateAlreadyExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.directoryservice#CertificateAlreadyExistsException``."""

    code: str | None = "CertificateAlreadyExistsException"

    def __init__(self, data: CertificateAlreadyExistsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CertificateAlreadyExistsException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "CertificateAlreadyExistsException":
        return cls(deserialize_aws_json_1_1(data))

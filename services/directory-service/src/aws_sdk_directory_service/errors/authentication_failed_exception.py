"""Generated from Smithy shape ``com.amazonaws.directoryservice#AuthenticationFailedException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_directory_service.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.exception_message
    import aws_sdk_directory_service.types.request_id


class AuthenticationFailedException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_directory_service.types.exception_message.ExceptionMessage"
    ]
    """<p>The textual message for the exception.</p>"""
    request_id: NotRequired["aws_sdk_directory_service.types.request_id.RequestId"]
    """<p>The identifier of the request that caused the exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AuthenticationFailedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AuthenticationFailedException_:
    out: AuthenticationFailedException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out


class AuthenticationFailedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.directoryservice#AuthenticationFailedException``."""

    code: str | None = "AuthenticationFailedException"

    def __init__(self, data: AuthenticationFailedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AuthenticationFailedException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "AuthenticationFailedException":
        return cls(deserialize_aws_json_1_1(data))

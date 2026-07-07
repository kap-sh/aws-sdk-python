"""Generated from Smithy shape ``com.amazonaws.apprunner#InternalServiceErrorException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_apprunner.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.error_message


class InternalServiceErrorException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_apprunner.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InternalServiceErrorException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InternalServiceErrorException_:
    out: InternalServiceErrorException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InternalServiceErrorException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.apprunner#InternalServiceErrorException``."""

    code: str | None = "InternalServiceErrorException"

    def __init__(self, data: InternalServiceErrorException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalServiceErrorException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "InternalServiceErrorException":
        return cls(deserialize_aws_json_1_0(data))

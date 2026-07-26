"""Generated from Smithy shape ``com.amazonaws.athena#InvalidRequestException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_athena.errors import ServiceError

if TYPE_CHECKING:
    import capo_athena.types.error_code
    import capo_athena.types.error_message


class InvalidRequestException_(TypedDict, closed=True):
    athena_error_code: NotRequired["capo_athena.types.error_code.ErrorCode"]
    message: NotRequired["capo_athena.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidRequestException_) -> dict:
    out: dict = {}
    if "athena_error_code" in value:
        out["AthenaErrorCode"] = value["athena_error_code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidRequestException_:
    out: InvalidRequestException_ = {}  # type: ignore[typeddict-item]
    if "AthenaErrorCode" in data:
        out["athena_error_code"] = data["AthenaErrorCode"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InvalidRequestException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.athena#InvalidRequestException``."""

    code: str | None = "InvalidRequestException"

    def __init__(self, data: InvalidRequestException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidRequestException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidRequestException":
        return cls(deserialize_aws_json_1_1(data))

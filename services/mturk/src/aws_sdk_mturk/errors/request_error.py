"""Generated from Smithy shape ``com.amazonaws.mturk#RequestError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mturk.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_mturk.types.exception_message
    import aws_sdk_mturk.types.turk_error_code


class RequestError_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_mturk.types.exception_message.ExceptionMessage"]
    turk_error_code: NotRequired["aws_sdk_mturk.types.turk_error_code.TurkErrorCode"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RequestError_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "turk_error_code" in value:
        out["TurkErrorCode"] = value["turk_error_code"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RequestError_:
    out: RequestError_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "TurkErrorCode" in data:
        out["turk_error_code"] = data["TurkErrorCode"]
    return out


class RequestError(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.mturk#RequestError``."""

    code: str | None = "RequestError"

    def __init__(self, data: RequestError_):
        super().__init__(
            "client", is_throttling_error=False, is_retryable=False, code="RequestError"
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "RequestError":
        return cls(deserialize_aws_json_1_1(data))

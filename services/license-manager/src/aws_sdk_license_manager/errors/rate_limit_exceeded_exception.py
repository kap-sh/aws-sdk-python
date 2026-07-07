"""Generated from Smithy shape ``com.amazonaws.licensemanager#RateLimitExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_license_manager.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.message


class RateLimitExceededException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_license_manager.types.message.Message"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RateLimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RateLimitExceededException_:
    out: RateLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class RateLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.licensemanager#RateLimitExceededException``."""

    code: str | None = "RateLimitExceededException"

    def __init__(self, data: RateLimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="RateLimitExceededException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "RateLimitExceededException":
        return cls(deserialize_aws_json_1_1(data))

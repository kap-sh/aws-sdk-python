"""Generated from Smithy shape ``com.amazonaws.pi#InternalServiceError``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_pi.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_pi.types.error_string


class InternalServiceError_(TypedDict):
    message: NotRequired["aws_sdk_pi.types.error_string.ErrorString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InternalServiceError_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InternalServiceError_:
    out: InternalServiceError_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InternalServiceError(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.pi#InternalServiceError``."""

    code: str | None = "InternalServiceError"

    def __init__(self, data: InternalServiceError_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalServiceError",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InternalServiceError":
        return cls(deserialize_aws_json_1_1(data))

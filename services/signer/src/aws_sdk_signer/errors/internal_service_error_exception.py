"""Generated from Smithy shape ``com.amazonaws.signer#InternalServiceErrorException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_signer.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_signer.types.error_code
    import aws_sdk_signer.types.error_message


class InternalServiceErrorException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_signer.types.error_message.ErrorMessage"]
    code: NotRequired["aws_sdk_signer.types.error_code.ErrorCode"]


# --- restJson1 ser/de ---
def serialize_json(value: InternalServiceErrorException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "code" in value:
        out["code"] = value["code"]
    return out


def deserialize_json(data: dict) -> InternalServiceErrorException_:
    out: InternalServiceErrorException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "code" in data:
        out["code"] = data["code"]
    return out


class InternalServiceErrorException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.signer#InternalServiceErrorException``."""

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
    def from_json(cls, data: dict) -> "InternalServiceErrorException":
        return cls(deserialize_json(data))

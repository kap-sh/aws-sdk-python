"""Generated from Smithy shape ``com.amazonaws.signer#ServiceLimitExceededException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_signer.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_signer.types.error_code
    import aws_sdk_signer.types.error_message


class ServiceLimitExceededException_(TypedDict):
    message: NotRequired["aws_sdk_signer.types.error_message.ErrorMessage"]
    code: NotRequired["aws_sdk_signer.types.error_code.ErrorCode"]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceLimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "code" in value:
        out["code"] = value["code"]
    return out


def deserialize_json(data: dict) -> ServiceLimitExceededException_:
    out: ServiceLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "code" in data:
        out["code"] = data["code"]
    return out


class ServiceLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.signer#ServiceLimitExceededException``."""

    code: str | None = "ServiceLimitExceededException"

    def __init__(self, data: ServiceLimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceLimitExceededException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ServiceLimitExceededException":
        return cls(deserialize_json(data))

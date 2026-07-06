"""Generated from Smithy shape ``com.amazonaws.apigateway#TooManyRequestsException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_api_gateway.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.string


class TooManyRequestsException_(TypedDict, closed=True):
    retry_after_seconds: NotRequired["aws_sdk_api_gateway.types.string.String"]
    message: NotRequired["aws_sdk_api_gateway.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: TooManyRequestsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> TooManyRequestsException_:
    out: TooManyRequestsException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class TooManyRequestsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.apigateway#TooManyRequestsException``."""

    code: str | None = "TooManyRequestsException"

    def __init__(self, data: TooManyRequestsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TooManyRequestsException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "TooManyRequestsException":
        return cls(deserialize_json(data))

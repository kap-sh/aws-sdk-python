"""Generated from Smithy shape ``com.amazonaws.apigatewaymanagementapi#PayloadTooLargeException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_apigatewaymanagementapi.errors import ServiceError

if TYPE_CHECKING:
    import capo_apigatewaymanagementapi.types.__string


class PayloadTooLargeException_(TypedDict, closed=True):
    message: NotRequired["capo_apigatewaymanagementapi.types.__string.__string"]


# --- restJson1 ser/de ---
def serialize_json(value: PayloadTooLargeException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> PayloadTooLargeException_:
    out: PayloadTooLargeException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class PayloadTooLargeException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.apigatewaymanagementapi#PayloadTooLargeException``."""

    code: str | None = "PayloadTooLargeException"

    def __init__(self, data: PayloadTooLargeException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PayloadTooLargeException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "PayloadTooLargeException":
        return cls(deserialize_json(data))

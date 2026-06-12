"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#TooManyRequestsException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_apigatewayv2.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string


class TooManyRequestsException_(TypedDict):
    limit_type: NotRequired["aws_sdk_apigatewayv2.types.__string.__string"]
    """<p>The limit type.</p>"""
    message: NotRequired["aws_sdk_apigatewayv2.types.__string.__string"]
    """<p>Describes the error encountered.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TooManyRequestsException_) -> dict:
    out: dict = {}
    if "limit_type" in value:
        out["limitType"] = value["limit_type"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> TooManyRequestsException_:
    out: TooManyRequestsException_ = {}  # type: ignore[typeddict-item]
    if "limitType" in data:
        out["limit_type"] = data["limitType"]
    if "message" in data:
        out["message"] = data["message"]
    return out


class TooManyRequestsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.apigatewayv2#TooManyRequestsException``."""

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

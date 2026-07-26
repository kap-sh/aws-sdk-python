"""Generated from Smithy shape ``com.amazonaws.sagemakerruntimehttp2#ServiceUnavailableError``."""

from typing_extensions import NotRequired, TypedDict

from capo_sagemaker_runtime_http2.errors import ServiceError


class ServiceUnavailableError_(TypedDict, closed=True):
    message: NotRequired["str"]
    """<p>Error message.</p>"""
    error_code: NotRequired["str"]
    """<p>Error code.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceUnavailableError_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    return out


def deserialize_json(data: dict) -> ServiceUnavailableError_:
    out: ServiceUnavailableError_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    return out


class ServiceUnavailableError(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sagemakerruntimehttp2#ServiceUnavailableError``."""

    code: str | None = "ServiceUnavailableError"

    def __init__(self, data: ServiceUnavailableError_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceUnavailableError",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ServiceUnavailableError":
        return cls(deserialize_json(data))

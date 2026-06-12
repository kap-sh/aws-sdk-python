"""Generated from Smithy shape ``com.amazonaws.sagemakerruntimehttp2#ModelStreamError``."""

from typing import TypedDict

from typing_extensions import NotRequired

from aws_sdk_sagemaker_runtime_http2.errors import ServiceError


class ModelStreamError_(TypedDict):
    message: NotRequired["str"]
    """<p>Error message.</p>"""
    error_code: NotRequired["str"]
    """<p>Error code.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ModelStreamError_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    return out


def deserialize_json(data: dict) -> ModelStreamError_:
    out: ModelStreamError_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    return out


class ModelStreamError(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sagemakerruntimehttp2#ModelStreamError``."""

    code: str | None = "ModelStreamError"

    def __init__(self, data: ModelStreamError_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ModelStreamError",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ModelStreamError":
        return cls(deserialize_json(data))

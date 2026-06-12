"""Generated from Smithy shape ``com.amazonaws.sagemakerruntimehttp2#InternalStreamFailure``."""

from typing import TypedDict

from typing_extensions import NotRequired

from aws_sdk_sagemaker_runtime_http2.errors import ServiceError


class InternalStreamFailure_(TypedDict):
    message: NotRequired["str"]
    """<p>Error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InternalStreamFailure_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InternalStreamFailure_:
    out: InternalStreamFailure_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InternalStreamFailure(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sagemakerruntimehttp2#InternalStreamFailure``."""

    code: str | None = "InternalStreamFailure"

    def __init__(self, data: InternalStreamFailure_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalStreamFailure",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InternalStreamFailure":
        return cls(deserialize_json(data))

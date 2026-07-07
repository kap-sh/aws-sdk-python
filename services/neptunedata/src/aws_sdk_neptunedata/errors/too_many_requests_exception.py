"""Generated from Smithy shape ``com.amazonaws.neptunedata#TooManyRequestsException``."""

from typing_extensions import TypedDict

from aws_sdk_neptunedata.errors import DeserializationError, ServiceError


class TooManyRequestsException_(TypedDict, closed=True):
    detailed_message: "str"
    """<p>A detailed message describing the problem.</p>"""
    request_id: "str"
    """<p>The ID of the request that could not be processed for this reason.</p>"""
    code: "str"
    """<p>The HTTP status code returned with the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TooManyRequestsException_) -> dict:
    out: dict = {}
    out["detailedMessage"] = value["detailed_message"]
    out["requestId"] = value["request_id"]
    out["code"] = value["code"]
    return out


def deserialize_json(data: dict) -> TooManyRequestsException_:
    out: TooManyRequestsException_ = {}  # type: ignore[typeddict-item]
    if "detailedMessage" in data:
        out["detailed_message"] = data["detailedMessage"]
    else:
        raise DeserializationError(
            "TooManyRequestsException_.detailed_message required"
        )
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    else:
        raise DeserializationError("TooManyRequestsException_.request_id required")
    if "code" in data:
        out["code"] = data["code"]
    else:
        raise DeserializationError("TooManyRequestsException_.code required")
    return out


class TooManyRequestsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.neptunedata#TooManyRequestsException``."""

    code: str | None = "TooManyRequestsException"

    def __init__(self, data: TooManyRequestsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=True,
            code="TooManyRequestsException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "TooManyRequestsException":
        return cls(deserialize_json(data))

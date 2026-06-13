"""Generated from Smithy shape ``com.amazonaws.neptunedata#TimeLimitExceededException``."""

from typing import TypedDict

from aws_sdk_neptunedata.errors import DeserializationError, ServiceError


class TimeLimitExceededException_(TypedDict):
    detailed_message: "str"
    """<p>A detailed message describing the problem.</p>"""
    request_id: "str"
    """<p>The ID of the request that could not be processed for this reason.</p>"""
    code: "str"
    """<p>The HTTP status code returned with the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimeLimitExceededException_) -> dict:
    out: dict = {}
    out["detailedMessage"] = value["detailed_message"]
    out["requestId"] = value["request_id"]
    out["code"] = value["code"]
    return out


def deserialize_json(data: dict) -> TimeLimitExceededException_:
    out: TimeLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "detailedMessage" in data:
        out["detailed_message"] = data["detailedMessage"]
    else:
        raise DeserializationError(
            "TimeLimitExceededException_.detailed_message required"
        )
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    else:
        raise DeserializationError("TimeLimitExceededException_.request_id required")
    if "code" in data:
        out["code"] = data["code"]
    else:
        raise DeserializationError("TimeLimitExceededException_.code required")
    return out


class TimeLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.neptunedata#TimeLimitExceededException``."""

    code: str | None = "TimeLimitExceededException"

    def __init__(self, data: TimeLimitExceededException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=True,
            code="TimeLimitExceededException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "TimeLimitExceededException":
        return cls(deserialize_json(data))

"""Generated from Smithy shape ``com.amazonaws.neptunedata#MemoryLimitExceededException``."""

from typing_extensions import TypedDict

from capo_neptunedata.errors import DeserializationError, ServiceError


class MemoryLimitExceededException_(TypedDict, closed=True):
    detailed_message: "str"
    """<p>A detailed message describing the problem.</p>"""
    request_id: "str"
    """<p>The ID of the request that failed.</p>"""
    code: "str"
    """<p>The HTTP status code returned with the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MemoryLimitExceededException_) -> dict:
    out: dict = {}
    out["detailedMessage"] = value["detailed_message"]
    out["requestId"] = value["request_id"]
    out["code"] = value["code"]
    return out


def deserialize_json(data: dict) -> MemoryLimitExceededException_:
    out: MemoryLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "detailedMessage" in data:
        out["detailed_message"] = data["detailedMessage"]
    else:
        raise DeserializationError(
            "MemoryLimitExceededException_.detailed_message required"
        )
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    else:
        raise DeserializationError("MemoryLimitExceededException_.request_id required")
    if "code" in data:
        out["code"] = data["code"]
    else:
        raise DeserializationError("MemoryLimitExceededException_.code required")
    return out


class MemoryLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.neptunedata#MemoryLimitExceededException``."""

    code: str | None = "MemoryLimitExceededException"

    def __init__(self, data: MemoryLimitExceededException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=True,
            code="MemoryLimitExceededException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "MemoryLimitExceededException":
        return cls(deserialize_json(data))

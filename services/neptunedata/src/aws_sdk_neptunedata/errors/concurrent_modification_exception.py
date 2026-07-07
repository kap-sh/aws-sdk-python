"""Generated from Smithy shape ``com.amazonaws.neptunedata#ConcurrentModificationException``."""

from typing_extensions import TypedDict

from aws_sdk_neptunedata.errors import DeserializationError, ServiceError


class ConcurrentModificationException_(TypedDict, closed=True):
    detailed_message: "str"
    """<p>A detailed message describing the problem.</p>"""
    request_id: "str"
    """<p>The ID of the request in question.</p>"""
    code: "str"
    """<p>The HTTP status code returned with the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConcurrentModificationException_) -> dict:
    out: dict = {}
    out["detailedMessage"] = value["detailed_message"]
    out["requestId"] = value["request_id"]
    out["code"] = value["code"]
    return out


def deserialize_json(data: dict) -> ConcurrentModificationException_:
    out: ConcurrentModificationException_ = {}  # type: ignore[typeddict-item]
    if "detailedMessage" in data:
        out["detailed_message"] = data["detailedMessage"]
    else:
        raise DeserializationError(
            "ConcurrentModificationException_.detailed_message required"
        )
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    else:
        raise DeserializationError(
            "ConcurrentModificationException_.request_id required"
        )
    if "code" in data:
        out["code"] = data["code"]
    else:
        raise DeserializationError("ConcurrentModificationException_.code required")
    return out


class ConcurrentModificationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.neptunedata#ConcurrentModificationException``."""

    code: str | None = "ConcurrentModificationException"

    def __init__(self, data: ConcurrentModificationException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=True,
            code="ConcurrentModificationException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ConcurrentModificationException":
        return cls(deserialize_json(data))

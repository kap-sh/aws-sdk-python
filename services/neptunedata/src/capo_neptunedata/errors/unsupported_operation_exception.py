"""Generated from Smithy shape ``com.amazonaws.neptunedata#UnsupportedOperationException``."""

from typing_extensions import TypedDict

from capo_neptunedata.errors import DeserializationError, ServiceError


class UnsupportedOperationException_(TypedDict, closed=True):
    detailed_message: "str"
    """<p>A detailed message describing the problem.</p>"""
    request_id: "str"
    """<p>The ID of the request in question.</p>"""
    code: "str"
    """<p>The HTTP status code returned with the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnsupportedOperationException_) -> dict:
    out: dict = {}
    out["detailedMessage"] = value["detailed_message"]
    out["requestId"] = value["request_id"]
    out["code"] = value["code"]
    return out


def deserialize_json(data: dict) -> UnsupportedOperationException_:
    out: UnsupportedOperationException_ = {}  # type: ignore[typeddict-item]
    if "detailedMessage" in data:
        out["detailed_message"] = data["detailedMessage"]
    else:
        raise DeserializationError(
            "UnsupportedOperationException_.detailed_message required"
        )
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    else:
        raise DeserializationError("UnsupportedOperationException_.request_id required")
    if "code" in data:
        out["code"] = data["code"]
    else:
        raise DeserializationError("UnsupportedOperationException_.code required")
    return out


class UnsupportedOperationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.neptunedata#UnsupportedOperationException``."""

    code: str | None = "UnsupportedOperationException"

    def __init__(self, data: UnsupportedOperationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnsupportedOperationException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "UnsupportedOperationException":
        return cls(deserialize_json(data))

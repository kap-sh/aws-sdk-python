"""Generated from Smithy shape ``com.amazonaws.neptunedata#ReadOnlyViolationException``."""

from typing import TypedDict

from aws_sdk_neptunedata.errors import DeserializationError, ServiceError


class ReadOnlyViolationException_(TypedDict):
    detailed_message: "str"
    """<p>A detailed message describing the problem.</p>"""
    request_id: "str"
    """<p>The ID of the request in which the parameter is missing.</p>"""
    code: "str"
    """<p>The HTTP status code returned with the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReadOnlyViolationException_) -> dict:
    out: dict = {}
    out["detailedMessage"] = value["detailed_message"]
    out["requestId"] = value["request_id"]
    out["code"] = value["code"]
    return out


def deserialize_json(data: dict) -> ReadOnlyViolationException_:
    out: ReadOnlyViolationException_ = {}  # type: ignore[typeddict-item]
    if "detailedMessage" in data:
        out["detailed_message"] = data["detailedMessage"]
    else:
        raise DeserializationError(
            "ReadOnlyViolationException_.detailed_message required"
        )
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    else:
        raise DeserializationError("ReadOnlyViolationException_.request_id required")
    if "code" in data:
        out["code"] = data["code"]
    else:
        raise DeserializationError("ReadOnlyViolationException_.code required")
    return out


class ReadOnlyViolationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.neptunedata#ReadOnlyViolationException``."""

    code: str | None = "ReadOnlyViolationException"

    def __init__(self, data: ReadOnlyViolationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ReadOnlyViolationException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ReadOnlyViolationException":
        return cls(deserialize_json(data))

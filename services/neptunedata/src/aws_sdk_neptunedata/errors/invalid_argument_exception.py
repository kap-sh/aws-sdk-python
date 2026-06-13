"""Generated from Smithy shape ``com.amazonaws.neptunedata#InvalidArgumentException``."""

from typing import TypedDict

from aws_sdk_neptunedata.errors import DeserializationError, ServiceError


class InvalidArgumentException_(TypedDict):
    detailed_message: "str"
    """<p>A detailed message describing the problem.</p>"""
    request_id: "str"
    """<p>The ID of the request in question.</p>"""
    code: "str"
    """<p>The HTTP status code returned with the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvalidArgumentException_) -> dict:
    out: dict = {}
    out["detailedMessage"] = value["detailed_message"]
    out["requestId"] = value["request_id"]
    out["code"] = value["code"]
    return out


def deserialize_json(data: dict) -> InvalidArgumentException_:
    out: InvalidArgumentException_ = {}  # type: ignore[typeddict-item]
    if "detailedMessage" in data:
        out["detailed_message"] = data["detailedMessage"]
    else:
        raise DeserializationError(
            "InvalidArgumentException_.detailed_message required"
        )
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    else:
        raise DeserializationError("InvalidArgumentException_.request_id required")
    if "code" in data:
        out["code"] = data["code"]
    else:
        raise DeserializationError("InvalidArgumentException_.code required")
    return out


class InvalidArgumentException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.neptunedata#InvalidArgumentException``."""

    code: str | None = "InvalidArgumentException"

    def __init__(self, data: InvalidArgumentException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidArgumentException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidArgumentException":
        return cls(deserialize_json(data))

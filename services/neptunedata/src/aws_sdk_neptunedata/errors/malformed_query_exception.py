"""Generated from Smithy shape ``com.amazonaws.neptunedata#MalformedQueryException``."""

from typing import TypedDict

from aws_sdk_neptunedata.errors import DeserializationError, ServiceError


class MalformedQueryException_(TypedDict):
    detailed_message: "str"
    """<p>A detailed message describing the problem.</p>"""
    request_id: "str"
    """<p>The ID of the malformed query request.</p>"""
    code: "str"
    """<p>The HTTP status code returned with the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MalformedQueryException_) -> dict:
    out: dict = {}
    out["detailedMessage"] = value["detailed_message"]
    out["requestId"] = value["request_id"]
    out["code"] = value["code"]
    return out


def deserialize_json(data: dict) -> MalformedQueryException_:
    out: MalformedQueryException_ = {}  # type: ignore[typeddict-item]
    if "detailedMessage" in data:
        out["detailed_message"] = data["detailedMessage"]
    else:
        raise DeserializationError("MalformedQueryException_.detailed_message required")
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    else:
        raise DeserializationError("MalformedQueryException_.request_id required")
    if "code" in data:
        out["code"] = data["code"]
    else:
        raise DeserializationError("MalformedQueryException_.code required")
    return out


class MalformedQueryException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.neptunedata#MalformedQueryException``."""

    code: str | None = "MalformedQueryException"

    def __init__(self, data: MalformedQueryException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="MalformedQueryException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "MalformedQueryException":
        return cls(deserialize_json(data))

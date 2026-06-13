"""Generated from Smithy shape ``com.amazonaws.neptunedata#ServerShutdownException``."""

from typing import TypedDict

from aws_sdk_neptunedata.errors import DeserializationError, ServiceError


class ServerShutdownException_(TypedDict):
    detailed_message: "str"
    """<p>A detailed message describing the problem.</p>"""
    request_id: "str"
    """<p>The ID of the request in question.</p>"""
    code: "str"
    """<p>The HTTP status code returned with the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServerShutdownException_) -> dict:
    out: dict = {}
    out["detailedMessage"] = value["detailed_message"]
    out["requestId"] = value["request_id"]
    out["code"] = value["code"]
    return out


def deserialize_json(data: dict) -> ServerShutdownException_:
    out: ServerShutdownException_ = {}  # type: ignore[typeddict-item]
    if "detailedMessage" in data:
        out["detailed_message"] = data["detailedMessage"]
    else:
        raise DeserializationError("ServerShutdownException_.detailed_message required")
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    else:
        raise DeserializationError("ServerShutdownException_.request_id required")
    if "code" in data:
        out["code"] = data["code"]
    else:
        raise DeserializationError("ServerShutdownException_.code required")
    return out


class ServerShutdownException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.neptunedata#ServerShutdownException``."""

    code: str | None = "ServerShutdownException"

    def __init__(self, data: ServerShutdownException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="ServerShutdownException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ServerShutdownException":
        return cls(deserialize_json(data))

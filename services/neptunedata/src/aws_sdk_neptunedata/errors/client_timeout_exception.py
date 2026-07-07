"""Generated from Smithy shape ``com.amazonaws.neptunedata#ClientTimeoutException``."""

from typing_extensions import TypedDict

from aws_sdk_neptunedata.errors import DeserializationError, ServiceError


class ClientTimeoutException_(TypedDict, closed=True):
    detailed_message: "str"
    """<p>A detailed message describing the problem.</p>"""
    request_id: "str"
    """<p>The ID of the request in question.</p>"""
    code: "str"
    """<p>The HTTP status code returned with the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClientTimeoutException_) -> dict:
    out: dict = {}
    out["detailedMessage"] = value["detailed_message"]
    out["requestId"] = value["request_id"]
    out["code"] = value["code"]
    return out


def deserialize_json(data: dict) -> ClientTimeoutException_:
    out: ClientTimeoutException_ = {}  # type: ignore[typeddict-item]
    if "detailedMessage" in data:
        out["detailed_message"] = data["detailedMessage"]
    else:
        raise DeserializationError("ClientTimeoutException_.detailed_message required")
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    else:
        raise DeserializationError("ClientTimeoutException_.request_id required")
    if "code" in data:
        out["code"] = data["code"]
    else:
        raise DeserializationError("ClientTimeoutException_.code required")
    return out


class ClientTimeoutException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.neptunedata#ClientTimeoutException``."""

    code: str | None = "ClientTimeoutException"

    def __init__(self, data: ClientTimeoutException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=True,
            code="ClientTimeoutException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ClientTimeoutException":
        return cls(deserialize_json(data))

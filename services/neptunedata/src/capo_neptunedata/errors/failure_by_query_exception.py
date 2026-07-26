"""Generated from Smithy shape ``com.amazonaws.neptunedata#FailureByQueryException``."""

from typing_extensions import TypedDict

from capo_neptunedata.errors import DeserializationError, ServiceError


class FailureByQueryException_(TypedDict, closed=True):
    detailed_message: "str"
    """<p>A detailed message describing the problem.</p>"""
    request_id: "str"
    """<p>The ID of the request in question.</p>"""
    code: "str"
    """<p>The HTTP status code returned with the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FailureByQueryException_) -> dict:
    out: dict = {}
    out["detailedMessage"] = value["detailed_message"]
    out["requestId"] = value["request_id"]
    out["code"] = value["code"]
    return out


def deserialize_json(data: dict) -> FailureByQueryException_:
    out: FailureByQueryException_ = {}  # type: ignore[typeddict-item]
    if "detailedMessage" in data:
        out["detailed_message"] = data["detailedMessage"]
    else:
        raise DeserializationError("FailureByQueryException_.detailed_message required")
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    else:
        raise DeserializationError("FailureByQueryException_.request_id required")
    if "code" in data:
        out["code"] = data["code"]
    else:
        raise DeserializationError("FailureByQueryException_.code required")
    return out


class FailureByQueryException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.neptunedata#FailureByQueryException``."""

    code: str | None = "FailureByQueryException"

    def __init__(self, data: FailureByQueryException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=True,
            code="FailureByQueryException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "FailureByQueryException":
        return cls(deserialize_json(data))

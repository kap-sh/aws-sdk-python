"""Generated from Smithy shape ``com.amazonaws.neptunedata#InvalidNumericDataException``."""

from typing_extensions import TypedDict

from capo_neptunedata.errors import DeserializationError, ServiceError


class InvalidNumericDataException_(TypedDict, closed=True):
    detailed_message: "str"
    """<p>A detailed message describing the problem.</p>"""
    request_id: "str"
    """<p>The ID of the request in question.</p>"""
    code: "str"
    """<p>The HTTP status code returned with the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvalidNumericDataException_) -> dict:
    out: dict = {}
    out["detailedMessage"] = value["detailed_message"]
    out["requestId"] = value["request_id"]
    out["code"] = value["code"]
    return out


def deserialize_json(data: dict) -> InvalidNumericDataException_:
    out: InvalidNumericDataException_ = {}  # type: ignore[typeddict-item]
    if "detailedMessage" in data:
        out["detailed_message"] = data["detailedMessage"]
    else:
        raise DeserializationError(
            "InvalidNumericDataException_.detailed_message required"
        )
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    else:
        raise DeserializationError("InvalidNumericDataException_.request_id required")
    if "code" in data:
        out["code"] = data["code"]
    else:
        raise DeserializationError("InvalidNumericDataException_.code required")
    return out


class InvalidNumericDataException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.neptunedata#InvalidNumericDataException``."""

    code: str | None = "InvalidNumericDataException"

    def __init__(self, data: InvalidNumericDataException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidNumericDataException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidNumericDataException":
        return cls(deserialize_json(data))

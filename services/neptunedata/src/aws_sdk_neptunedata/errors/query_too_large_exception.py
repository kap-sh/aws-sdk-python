"""Generated from Smithy shape ``com.amazonaws.neptunedata#QueryTooLargeException``."""

from typing_extensions import TypedDict

from aws_sdk_neptunedata.errors import DeserializationError, ServiceError


class QueryTooLargeException_(TypedDict, closed=True):
    detailed_message: "str"
    """<p>A detailed message describing the problem.</p>"""
    request_id: "str"
    """<p>The ID of the request that is too large.</p>"""
    code: "str"
    """<p>The HTTP status code returned with the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryTooLargeException_) -> dict:
    out: dict = {}
    out["detailedMessage"] = value["detailed_message"]
    out["requestId"] = value["request_id"]
    out["code"] = value["code"]
    return out


def deserialize_json(data: dict) -> QueryTooLargeException_:
    out: QueryTooLargeException_ = {}  # type: ignore[typeddict-item]
    if "detailedMessage" in data:
        out["detailed_message"] = data["detailedMessage"]
    else:
        raise DeserializationError("QueryTooLargeException_.detailed_message required")
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    else:
        raise DeserializationError("QueryTooLargeException_.request_id required")
    if "code" in data:
        out["code"] = data["code"]
    else:
        raise DeserializationError("QueryTooLargeException_.code required")
    return out


class QueryTooLargeException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.neptunedata#QueryTooLargeException``."""

    code: str | None = "QueryTooLargeException"

    def __init__(self, data: QueryTooLargeException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="QueryTooLargeException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "QueryTooLargeException":
        return cls(deserialize_json(data))

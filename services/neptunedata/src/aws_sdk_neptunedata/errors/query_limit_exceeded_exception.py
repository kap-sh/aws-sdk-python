"""Generated from Smithy shape ``com.amazonaws.neptunedata#QueryLimitExceededException``."""

from typing_extensions import TypedDict

from aws_sdk_neptunedata.errors import DeserializationError, ServiceError


class QueryLimitExceededException_(TypedDict, closed=True):
    detailed_message: "str"
    """<p>A detailed message describing the problem.</p>"""
    request_id: "str"
    """<p>The ID of the request which exceeded the limit.</p>"""
    code: "str"
    """<p>The HTTP status code returned with the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryLimitExceededException_) -> dict:
    out: dict = {}
    out["detailedMessage"] = value["detailed_message"]
    out["requestId"] = value["request_id"]
    out["code"] = value["code"]
    return out


def deserialize_json(data: dict) -> QueryLimitExceededException_:
    out: QueryLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "detailedMessage" in data:
        out["detailed_message"] = data["detailedMessage"]
    else:
        raise DeserializationError(
            "QueryLimitExceededException_.detailed_message required"
        )
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    else:
        raise DeserializationError("QueryLimitExceededException_.request_id required")
    if "code" in data:
        out["code"] = data["code"]
    else:
        raise DeserializationError("QueryLimitExceededException_.code required")
    return out


class QueryLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.neptunedata#QueryLimitExceededException``."""

    code: str | None = "QueryLimitExceededException"

    def __init__(self, data: QueryLimitExceededException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=True,
            code="QueryLimitExceededException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "QueryLimitExceededException":
        return cls(deserialize_json(data))

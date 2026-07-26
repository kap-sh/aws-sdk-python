"""Generated from Smithy shape ``com.amazonaws.neptunedata#S3Exception``."""

from typing_extensions import TypedDict

from capo_neptunedata.errors import DeserializationError, ServiceError


class S3Exception_(TypedDict, closed=True):
    detailed_message: "str"
    """<p>A detailed message describing the problem.</p>"""
    request_id: "str"
    """<p>The ID of the request in question.</p>"""
    code: "str"
    """<p>The HTTP status code returned with the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Exception_) -> dict:
    out: dict = {}
    out["detailedMessage"] = value["detailed_message"]
    out["requestId"] = value["request_id"]
    out["code"] = value["code"]
    return out


def deserialize_json(data: dict) -> S3Exception_:
    out: S3Exception_ = {}  # type: ignore[typeddict-item]
    if "detailedMessage" in data:
        out["detailed_message"] = data["detailedMessage"]
    else:
        raise DeserializationError("S3Exception_.detailed_message required")
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    else:
        raise DeserializationError("S3Exception_.request_id required")
    if "code" in data:
        out["code"] = data["code"]
    else:
        raise DeserializationError("S3Exception_.code required")
    return out


class S3Exception(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.neptunedata#S3Exception``."""

    code: str | None = "S3Exception"

    def __init__(self, data: S3Exception_):
        super().__init__(
            "client", is_throttling_error=False, is_retryable=True, code="S3Exception"
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "S3Exception":
        return cls(deserialize_json(data))

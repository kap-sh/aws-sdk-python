"""Generated from Smithy shape ``com.amazonaws.neptunedata#BulkLoadIdNotFoundException``."""

from typing import TypedDict
from aws_sdk_neptunedata.errors import DeserializationError
from aws_sdk_neptunedata.errors import ServiceError

class BulkLoadIdNotFoundException_(TypedDict):
    detailed_message: "str"
    """<p>A detailed message describing the problem.</p>"""
    request_id: "str"
    """<p>The bulk-load job ID that could not be found.</p>"""
    code: "str"
    """<p>The HTTP status code returned with the exception.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: BulkLoadIdNotFoundException_) -> dict:
    out: dict = {}
    out["detailedMessage"] = value["detailed_message"]
    out["requestId"] = value["request_id"]
    out["code"] = value["code"]
    return out


def deserialize_json(data: dict) -> BulkLoadIdNotFoundException_:
    out: BulkLoadIdNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "detailedMessage" in data:
        out["detailed_message"] = data["detailedMessage"]
    else:
        raise DeserializationError("BulkLoadIdNotFoundException_.detailed_message required")
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    else:
        raise DeserializationError("BulkLoadIdNotFoundException_.request_id required")
    if "code" in data:
        out["code"] = data["code"]
    else:
        raise DeserializationError("BulkLoadIdNotFoundException_.code required")
    return out


class BulkLoadIdNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.neptunedata#BulkLoadIdNotFoundException``."""
    code: str | None = 'BulkLoadIdNotFoundException'

    def __init__(self, data: BulkLoadIdNotFoundException_):
        super().__init__('client', is_throttling_error=False, is_retryable=True, code='BulkLoadIdNotFoundException')
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "BulkLoadIdNotFoundException":
        return cls(deserialize_json(data))
"""Generated from Smithy shape ``com.amazonaws.neptunedata#InvalidParameterException``."""

from typing import TypedDict

from aws_sdk_neptunedata.errors import DeserializationError, ServiceError


class InvalidParameterException_(TypedDict):
    detailed_message: "str"
    """<p>A detailed message describing the problem.</p>"""
    request_id: "str"
    """<p>The ID of the request that includes an invalid parameter.</p>"""
    code: "str"
    """<p>The HTTP status code returned with the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvalidParameterException_) -> dict:
    out: dict = {}
    out["detailedMessage"] = value["detailed_message"]
    out["requestId"] = value["request_id"]
    out["code"] = value["code"]
    return out


def deserialize_json(data: dict) -> InvalidParameterException_:
    out: InvalidParameterException_ = {}  # type: ignore[typeddict-item]
    if "detailedMessage" in data:
        out["detailed_message"] = data["detailedMessage"]
    else:
        raise DeserializationError(
            "InvalidParameterException_.detailed_message required"
        )
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    else:
        raise DeserializationError("InvalidParameterException_.request_id required")
    if "code" in data:
        out["code"] = data["code"]
    else:
        raise DeserializationError("InvalidParameterException_.code required")
    return out


class InvalidParameterException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.neptunedata#InvalidParameterException``."""

    code: str | None = "InvalidParameterException"

    def __init__(self, data: InvalidParameterException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidParameterException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidParameterException":
        return cls(deserialize_json(data))

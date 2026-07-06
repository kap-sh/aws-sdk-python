"""Generated from Smithy shape ``com.amazonaws.neptunedata#MissingParameterException``."""

from typing_extensions import TypedDict

from aws_sdk_neptunedata.errors import DeserializationError, ServiceError


class MissingParameterException_(TypedDict, closed=True):
    detailed_message: "str"
    """<p>A detailed message describing the problem.</p>"""
    request_id: "str"
    """<p>The ID of the request in which the parameter is missing.</p>"""
    code: "str"
    """<p>The HTTP status code returned with the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MissingParameterException_) -> dict:
    out: dict = {}
    out["detailedMessage"] = value["detailed_message"]
    out["requestId"] = value["request_id"]
    out["code"] = value["code"]
    return out


def deserialize_json(data: dict) -> MissingParameterException_:
    out: MissingParameterException_ = {}  # type: ignore[typeddict-item]
    if "detailedMessage" in data:
        out["detailed_message"] = data["detailedMessage"]
    else:
        raise DeserializationError(
            "MissingParameterException_.detailed_message required"
        )
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    else:
        raise DeserializationError("MissingParameterException_.request_id required")
    if "code" in data:
        out["code"] = data["code"]
    else:
        raise DeserializationError("MissingParameterException_.code required")
    return out


class MissingParameterException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.neptunedata#MissingParameterException``."""

    code: str | None = "MissingParameterException"

    def __init__(self, data: MissingParameterException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="MissingParameterException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "MissingParameterException":
        return cls(deserialize_json(data))

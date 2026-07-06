"""Generated from Smithy shape ``com.amazonaws.pinpoint#BadRequestException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_pinpoint.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string


class BadRequestException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The message that's returned from the API.</p>"""
    request_id: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the request or response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BadRequestException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "request_id" in value:
        out["RequestID"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> BadRequestException_:
    out: BadRequestException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "RequestID" in data:
        out["request_id"] = data["RequestID"]
    return out


class BadRequestException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.pinpoint#BadRequestException``."""

    code: str | None = "BadRequestException"

    def __init__(self, data: BadRequestException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="BadRequestException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "BadRequestException":
        return cls(deserialize_json(data))

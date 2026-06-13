"""Generated from Smithy shape ``com.amazonaws.quicksight#SessionLifetimeInMinutesInvalidException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.string


class SessionLifetimeInMinutesInvalidException_(TypedDict):
    message: NotRequired["aws_sdk_quicksight.types.string.String"]
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SessionLifetimeInMinutesInvalidException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> SessionLifetimeInMinutesInvalidException_:
    out: SessionLifetimeInMinutesInvalidException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out


class SessionLifetimeInMinutesInvalidException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.quicksight#SessionLifetimeInMinutesInvalidException``."""

    code: str | None = "SessionLifetimeInMinutesInvalidException"

    def __init__(self, data: SessionLifetimeInMinutesInvalidException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="SessionLifetimeInMinutesInvalidException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "SessionLifetimeInMinutesInvalidException":
        return cls(deserialize_json(data))

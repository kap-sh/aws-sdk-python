"""Generated from Smithy shape ``com.amazonaws.pinpoint#NotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pinpoint.errors import ServiceError

if TYPE_CHECKING:
    import capo_pinpoint.types.__string


class NotFoundException_(TypedDict, closed=True):
    message: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The message that's returned from the API.</p>"""
    request_id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the request or response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "request_id" in value:
        out["RequestID"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> NotFoundException_:
    out: NotFoundException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "RequestID" in data:
        out["request_id"] = data["RequestID"]
    return out


class NotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.pinpoint#NotFoundException``."""

    code: str | None = "NotFoundException"

    def __init__(self, data: NotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NotFoundException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "NotFoundException":
        return cls(deserialize_json(data))

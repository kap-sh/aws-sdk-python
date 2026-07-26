"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#ThrottlingException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_chime_sdk_meetings.errors import ServiceError

if TYPE_CHECKING:
    import capo_chime_sdk_meetings.types.string


class ThrottlingException_(TypedDict, closed=True):
    code: NotRequired["capo_chime_sdk_meetings.types.string.String"]
    message: NotRequired["capo_chime_sdk_meetings.types.string.String"]
    request_id: NotRequired["capo_chime_sdk_meetings.types.string.String"]
    """<p>The ID of the request that exceeded the throttling limit.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThrottlingException_) -> dict:
    out: dict = {}
    if "code" in value:
        out["Code"] = value["code"]
    if "message" in value:
        out["Message"] = value["message"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> ThrottlingException_:
    out: ThrottlingException_ = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        out["code"] = data["Code"]
    if "Message" in data:
        out["message"] = data["Message"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out


class ThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.chimesdkmeetings#ThrottlingException``."""

    code: str | None = "ThrottlingException"

    def __init__(self, data: ThrottlingException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ThrottlingException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ThrottlingException":
        return cls(deserialize_json(data))

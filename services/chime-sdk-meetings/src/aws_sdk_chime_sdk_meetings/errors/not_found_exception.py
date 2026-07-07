"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#NotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_chime_sdk_meetings.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_meetings.types.string


class NotFoundException_(TypedDict, closed=True):
    code: NotRequired["aws_sdk_chime_sdk_meetings.types.string.String"]
    message: NotRequired["aws_sdk_chime_sdk_meetings.types.string.String"]
    request_id: NotRequired["aws_sdk_chime_sdk_meetings.types.string.String"]
    """<p>The request ID associated with the call responsible for the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotFoundException_) -> dict:
    out: dict = {}
    if "code" in value:
        out["Code"] = value["code"]
    if "message" in value:
        out["Message"] = value["message"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> NotFoundException_:
    out: NotFoundException_ = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        out["code"] = data["Code"]
    if "Message" in data:
        out["message"] = data["Message"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out


class NotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.chimesdkmeetings#NotFoundException``."""

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

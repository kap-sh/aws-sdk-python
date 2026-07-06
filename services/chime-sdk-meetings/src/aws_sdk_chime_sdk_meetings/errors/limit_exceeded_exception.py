"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#LimitExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_chime_sdk_meetings.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_meetings.types.string


class LimitExceededException_(TypedDict, closed=True):
    code: NotRequired["aws_sdk_chime_sdk_meetings.types.string.String"]
    message: NotRequired["aws_sdk_chime_sdk_meetings.types.string.String"]
    request_id: NotRequired["aws_sdk_chime_sdk_meetings.types.string.String"]
    """<p>The request id associated with the call responsible for the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LimitExceededException_) -> dict:
    out: dict = {}
    if "code" in value:
        out["Code"] = value["code"]
    if "message" in value:
        out["Message"] = value["message"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> LimitExceededException_:
    out: LimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        out["code"] = data["Code"]
    if "Message" in data:
        out["message"] = data["Message"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out


class LimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.chimesdkmeetings#LimitExceededException``."""

    code: str | None = "LimitExceededException"

    def __init__(self, data: LimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="LimitExceededException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "LimitExceededException":
        return cls(deserialize_json(data))

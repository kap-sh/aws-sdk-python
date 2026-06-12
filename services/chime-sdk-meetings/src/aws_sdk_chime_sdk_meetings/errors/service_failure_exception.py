"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#ServiceFailureException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_chime_sdk_meetings.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_meetings.types.string


class ServiceFailureException_(TypedDict):
    code: NotRequired["aws_sdk_chime_sdk_meetings.types.string.String"]
    message: NotRequired["aws_sdk_chime_sdk_meetings.types.string.String"]
    request_id: NotRequired["aws_sdk_chime_sdk_meetings.types.string.String"]
    """<p>The ID of the failed request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceFailureException_) -> dict:
    out: dict = {}
    if "code" in value:
        out["Code"] = value["code"]
    if "message" in value:
        out["Message"] = value["message"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> ServiceFailureException_:
    out: ServiceFailureException_ = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        out["code"] = data["Code"]
    if "Message" in data:
        out["message"] = data["Message"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out


class ServiceFailureException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.chimesdkmeetings#ServiceFailureException``."""

    code: str | None = "ServiceFailureException"

    def __init__(self, data: ServiceFailureException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceFailureException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ServiceFailureException":
        return cls(deserialize_json(data))

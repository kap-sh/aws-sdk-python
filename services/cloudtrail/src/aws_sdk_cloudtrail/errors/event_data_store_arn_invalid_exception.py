"""Generated from Smithy shape ``com.amazonaws.cloudtrail#EventDataStoreARNInvalidException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudtrail.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.error_message


class EventDataStoreARNInvalidException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_cloudtrail.types.error_message.ErrorMessage"]
    """<p>Brief description of the exception returned by the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventDataStoreARNInvalidException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EventDataStoreARNInvalidException_:
    out: EventDataStoreARNInvalidException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class EventDataStoreARNInvalidException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudtrail#EventDataStoreARNInvalidException``."""

    code: str | None = "EventDataStoreARNInvalidException"

    def __init__(self, data: EventDataStoreARNInvalidException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="EventDataStoreARNInvalidException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "EventDataStoreARNInvalidException":
        return cls(deserialize_aws_json_1_1(data))

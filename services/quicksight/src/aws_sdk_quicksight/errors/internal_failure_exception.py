"""Generated from Smithy shape ``com.amazonaws.quicksight#InternalFailureException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.string


class InternalFailureException_(TypedDict):
    message: NotRequired["aws_sdk_quicksight.types.string.String"]
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InternalFailureException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> InternalFailureException_:
    out: InternalFailureException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out


class InternalFailureException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.quicksight#InternalFailureException``."""

    code: str | None = "InternalFailureException"

    def __init__(self, data: InternalFailureException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalFailureException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InternalFailureException":
        return cls(deserialize_json(data))

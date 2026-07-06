"""Generated from Smithy shape ``com.amazonaws.quicksight#CustomerManagedKeyUnavailableException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.string


class CustomerManagedKeyUnavailableException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_quicksight.types.string.String"]
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomerManagedKeyUnavailableException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> CustomerManagedKeyUnavailableException_:
    out: CustomerManagedKeyUnavailableException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out


class CustomerManagedKeyUnavailableException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.quicksight#CustomerManagedKeyUnavailableException``."""

    code: str | None = "CustomerManagedKeyUnavailableException"

    def __init__(self, data: CustomerManagedKeyUnavailableException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CustomerManagedKeyUnavailableException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "CustomerManagedKeyUnavailableException":
        return cls(deserialize_json(data))

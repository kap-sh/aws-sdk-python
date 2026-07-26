"""Generated from Smithy shape ``com.amazonaws.quicksight#PreconditionNotMetException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import ServiceError

if TYPE_CHECKING:
    import capo_quicksight.types.string


class PreconditionNotMetException_(TypedDict, closed=True):
    message: NotRequired["capo_quicksight.types.string.String"]
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PreconditionNotMetException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> PreconditionNotMetException_:
    out: PreconditionNotMetException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out


class PreconditionNotMetException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.quicksight#PreconditionNotMetException``."""

    code: str | None = "PreconditionNotMetException"

    def __init__(self, data: PreconditionNotMetException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PreconditionNotMetException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "PreconditionNotMetException":
        return cls(deserialize_json(data))

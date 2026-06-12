"""Generated from Smithy shape ``com.amazonaws.lakeformation#TransactionCommitInProgressException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lakeformation.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.message_string


class TransactionCommitInProgressException_(TypedDict):
    message: NotRequired["aws_sdk_lakeformation.types.message_string.MessageString"]
    """<p>A message describing the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TransactionCommitInProgressException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> TransactionCommitInProgressException_:
    out: TransactionCommitInProgressException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class TransactionCommitInProgressException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lakeformation#TransactionCommitInProgressException``."""

    code: str | None = "TransactionCommitInProgressException"

    def __init__(self, data: TransactionCommitInProgressException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TransactionCommitInProgressException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "TransactionCommitInProgressException":
        return cls(deserialize_json(data))

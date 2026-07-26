"""Generated from Smithy shape ``com.amazonaws.lakeformation#TransactionCanceledException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lakeformation.errors import ServiceError

if TYPE_CHECKING:
    import capo_lakeformation.types.message_string


class TransactionCanceledException_(TypedDict, closed=True):
    message: NotRequired["capo_lakeformation.types.message_string.MessageString"]
    """<p>A message describing the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TransactionCanceledException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> TransactionCanceledException_:
    out: TransactionCanceledException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class TransactionCanceledException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lakeformation#TransactionCanceledException``."""

    code: str | None = "TransactionCanceledException"

    def __init__(self, data: TransactionCanceledException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TransactionCanceledException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "TransactionCanceledException":
        return cls(deserialize_json(data))

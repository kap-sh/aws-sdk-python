"""Generated from Smithy shape ``com.amazonaws.lakeformation#TransactionCommittedException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lakeformation.errors import ServiceError

if TYPE_CHECKING:
    import capo_lakeformation.types.message_string


class TransactionCommittedException_(TypedDict, closed=True):
    message: NotRequired["capo_lakeformation.types.message_string.MessageString"]
    """<p>A message describing the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TransactionCommittedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> TransactionCommittedException_:
    out: TransactionCommittedException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class TransactionCommittedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lakeformation#TransactionCommittedException``."""

    code: str | None = "TransactionCommittedException"

    def __init__(self, data: TransactionCommittedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TransactionCommittedException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "TransactionCommittedException":
        return cls(deserialize_json(data))

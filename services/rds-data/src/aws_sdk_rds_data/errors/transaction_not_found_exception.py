"""Generated from Smithy shape ``com.amazonaws.rdsdata#TransactionNotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds_data.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_rds_data.types.error_message


class TransactionNotFoundException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_rds_data.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: TransactionNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> TransactionNotFoundException_:
    out: TransactionNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class TransactionNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.rdsdata#TransactionNotFoundException``."""

    code: str | None = "TransactionNotFoundException"

    def __init__(self, data: TransactionNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TransactionNotFoundException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "TransactionNotFoundException":
        return cls(deserialize_json(data))

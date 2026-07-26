"""Generated from Smithy shape ``com.amazonaws.workdocs#StorageLimitExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_workdocs.errors import ServiceError

if TYPE_CHECKING:
    import capo_workdocs.types.error_message_type


class StorageLimitExceededException_(TypedDict, closed=True):
    message: NotRequired["capo_workdocs.types.error_message_type.ErrorMessageType"]


# --- restJson1 ser/de ---
def serialize_json(value: StorageLimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> StorageLimitExceededException_:
    out: StorageLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class StorageLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workdocs#StorageLimitExceededException``."""

    code: str | None = "StorageLimitExceededException"

    def __init__(self, data: StorageLimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="StorageLimitExceededException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "StorageLimitExceededException":
        return cls(deserialize_json(data))

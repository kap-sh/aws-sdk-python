"""Generated from Smithy shape ``com.amazonaws.rdsdata#InvalidResourceStateException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds_data.errors import ServiceError

if TYPE_CHECKING:
    import capo_rds_data.types.error_message


class InvalidResourceStateException_(TypedDict, closed=True):
    message: NotRequired["capo_rds_data.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: InvalidResourceStateException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidResourceStateException_:
    out: InvalidResourceStateException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidResourceStateException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.rdsdata#InvalidResourceStateException``."""

    code: str | None = "InvalidResourceStateException"

    def __init__(self, data: InvalidResourceStateException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidResourceStateException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidResourceStateException":
        return cls(deserialize_json(data))

"""Generated from Smithy shape ``com.amazonaws.qbusiness#ThrottlingException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_qbusiness.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_qbusiness.types.error_message


class ThrottlingException_(TypedDict, closed=True):
    message: "capo_qbusiness.types.error_message.ErrorMessage"


# --- restJson1 ser/de ---
def serialize_json(value: ThrottlingException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ThrottlingException_:
    out: ThrottlingException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ThrottlingException_.message required")
    return out


class ThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.qbusiness#ThrottlingException``."""

    code: str | None = "ThrottlingException"

    def __init__(self, data: ThrottlingException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ThrottlingException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ThrottlingException":
        return cls(deserialize_json(data))

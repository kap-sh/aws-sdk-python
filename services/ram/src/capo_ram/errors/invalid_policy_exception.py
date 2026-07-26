"""Generated from Smithy shape ``com.amazonaws.ram#InvalidPolicyException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ram.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_ram.types.string


class InvalidPolicyException_(TypedDict, closed=True):
    message: "capo_ram.types.string.String"


# --- restJson1 ser/de ---
def serialize_json(value: InvalidPolicyException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidPolicyException_:
    out: InvalidPolicyException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("InvalidPolicyException_.message required")
    return out


class InvalidPolicyException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ram#InvalidPolicyException``."""

    code: str | None = "InvalidPolicyException"

    def __init__(self, data: InvalidPolicyException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidPolicyException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidPolicyException":
        return cls(deserialize_json(data))

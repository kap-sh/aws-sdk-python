"""Generated from Smithy shape ``com.amazonaws.ram#IdempotentParameterMismatchException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ram.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_ram.types.string


class IdempotentParameterMismatchException_(TypedDict, closed=True):
    message: "capo_ram.types.string.String"


# --- restJson1 ser/de ---
def serialize_json(value: IdempotentParameterMismatchException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> IdempotentParameterMismatchException_:
    out: IdempotentParameterMismatchException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError(
            "IdempotentParameterMismatchException_.message required"
        )
    return out


class IdempotentParameterMismatchException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ram#IdempotentParameterMismatchException``."""

    code: str | None = "IdempotentParameterMismatchException"

    def __init__(self, data: IdempotentParameterMismatchException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="IdempotentParameterMismatchException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "IdempotentParameterMismatchException":
        return cls(deserialize_json(data))

"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#ConflictException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_migrationhubstrategy.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.string


class ConflictException_(TypedDict, closed=True):
    message: "capo_migrationhubstrategy.types.string.String"


# --- restJson1 ser/de ---
def serialize_json(value: ConflictException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ConflictException_.message required")
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.migrationhubstrategy#ConflictException``."""

    code: str | None = "ConflictException"

    def __init__(self, data: ConflictException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConflictException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ConflictException":
        return cls(deserialize_json(data))

"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#ValidationException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_migration_hub_refactor_spaces.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_migration_hub_refactor_spaces.types.string


class ValidationException_(TypedDict, closed=True):
    message: "capo_migration_hub_refactor_spaces.types.string.String"


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("ValidationException_.message required")
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.migrationhubrefactorspaces#ValidationException``."""

    code: str | None = "ValidationException"

    def __init__(self, data: ValidationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ValidationException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ValidationException":
        return cls(deserialize_json(data))

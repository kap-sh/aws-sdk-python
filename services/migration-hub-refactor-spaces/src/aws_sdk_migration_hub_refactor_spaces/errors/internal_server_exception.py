"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#InternalServerException``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_migration_hub_refactor_spaces.errors import (
    DeserializationError,
    ServiceError,
)

if TYPE_CHECKING:
    import aws_sdk_migration_hub_refactor_spaces.types.string


class InternalServerException_(TypedDict):
    message: "aws_sdk_migration_hub_refactor_spaces.types.string.String"


# --- restJson1 ser/de ---
def serialize_json(value: InternalServerException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InternalServerException_:
    out: InternalServerException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("InternalServerException_.message required")
    return out


class InternalServerException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.migrationhubrefactorspaces#InternalServerException``."""

    code: str | None = "InternalServerException"

    def __init__(self, data: InternalServerException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalServerException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InternalServerException":
        return cls(deserialize_json(data))

"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#InvalidResourcePolicyException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_migration_hub_refactor_spaces.errors import (
    DeserializationError,
    ServiceError,
)

if TYPE_CHECKING:
    import aws_sdk_migration_hub_refactor_spaces.types.string


class InvalidResourcePolicyException_(TypedDict, closed=True):
    message: "aws_sdk_migration_hub_refactor_spaces.types.string.String"


# --- restJson1 ser/de ---
def serialize_json(value: InvalidResourcePolicyException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidResourcePolicyException_:
    out: InvalidResourcePolicyException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("InvalidResourcePolicyException_.message required")
    return out


class InvalidResourcePolicyException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.migrationhubrefactorspaces#InvalidResourcePolicyException``."""

    code: str | None = "InvalidResourcePolicyException"

    def __init__(self, data: InvalidResourcePolicyException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidResourcePolicyException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidResourcePolicyException":
        return cls(deserialize_json(data))

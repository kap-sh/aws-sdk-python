"""Generated from Smithy shape ``com.amazonaws.ram#PermissionVersionsLimitExceededException``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ram.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_ram.types.string


class PermissionVersionsLimitExceededException_(TypedDict):
    message: "aws_sdk_ram.types.string.String"


# --- restJson1 ser/de ---
def serialize_json(value: PermissionVersionsLimitExceededException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> PermissionVersionsLimitExceededException_:
    out: PermissionVersionsLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError(
            "PermissionVersionsLimitExceededException_.message required"
        )
    return out


class PermissionVersionsLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ram#PermissionVersionsLimitExceededException``."""

    code: str | None = "PermissionVersionsLimitExceededException"

    def __init__(self, data: PermissionVersionsLimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PermissionVersionsLimitExceededException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "PermissionVersionsLimitExceededException":
        return cls(deserialize_json(data))

"""Generated from Smithy shape ``com.amazonaws.ram#PermissionLimitExceededException``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ram.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_ram.types.string


class PermissionLimitExceededException_(TypedDict):
    message: "aws_sdk_ram.types.string.String"


# --- restJson1 ser/de ---
def serialize_json(value: PermissionLimitExceededException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> PermissionLimitExceededException_:
    out: PermissionLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("PermissionLimitExceededException_.message required")
    return out


class PermissionLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ram#PermissionLimitExceededException``."""

    code: str | None = "PermissionLimitExceededException"

    def __init__(self, data: PermissionLimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PermissionLimitExceededException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "PermissionLimitExceededException":
        return cls(deserialize_json(data))

"""Generated from Smithy shape ``com.amazonaws.ram#PermissionAlreadyExistsException``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ram.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_ram.types.string


class PermissionAlreadyExistsException_(TypedDict):
    message: "aws_sdk_ram.types.string.String"


# --- restJson1 ser/de ---
def serialize_json(value: PermissionAlreadyExistsException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> PermissionAlreadyExistsException_:
    out: PermissionAlreadyExistsException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("PermissionAlreadyExistsException_.message required")
    return out


class PermissionAlreadyExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ram#PermissionAlreadyExistsException``."""

    code: str | None = "PermissionAlreadyExistsException"

    def __init__(self, data: PermissionAlreadyExistsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PermissionAlreadyExistsException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "PermissionAlreadyExistsException":
        return cls(deserialize_json(data))

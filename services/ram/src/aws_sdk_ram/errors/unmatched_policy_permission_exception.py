"""Generated from Smithy shape ``com.amazonaws.ram#UnmatchedPolicyPermissionException``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ram.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_ram.types.string


class UnmatchedPolicyPermissionException_(TypedDict):
    message: "aws_sdk_ram.types.string.String"


# --- restJson1 ser/de ---
def serialize_json(value: UnmatchedPolicyPermissionException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> UnmatchedPolicyPermissionException_:
    out: UnmatchedPolicyPermissionException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError(
            "UnmatchedPolicyPermissionException_.message required"
        )
    return out


class UnmatchedPolicyPermissionException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ram#UnmatchedPolicyPermissionException``."""

    code: str | None = "UnmatchedPolicyPermissionException"

    def __init__(self, data: UnmatchedPolicyPermissionException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnmatchedPolicyPermissionException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "UnmatchedPolicyPermissionException":
        return cls(deserialize_json(data))

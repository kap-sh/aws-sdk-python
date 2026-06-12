"""Generated from Smithy shape ``com.amazonaws.ram#ResourceShareInvitationAlreadyRejectedException``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ram.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_ram.types.string


class ResourceShareInvitationAlreadyRejectedException_(TypedDict):
    message: "aws_sdk_ram.types.string.String"


# --- restJson1 ser/de ---
def serialize_json(value: ResourceShareInvitationAlreadyRejectedException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ResourceShareInvitationAlreadyRejectedException_:
    out: ResourceShareInvitationAlreadyRejectedException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError(
            "ResourceShareInvitationAlreadyRejectedException_.message required"
        )
    return out


class ResourceShareInvitationAlreadyRejectedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ram#ResourceShareInvitationAlreadyRejectedException``."""

    code: str | None = "ResourceShareInvitationAlreadyRejectedException"

    def __init__(self, data: ResourceShareInvitationAlreadyRejectedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceShareInvitationAlreadyRejectedException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ResourceShareInvitationAlreadyRejectedException":
        return cls(deserialize_json(data))

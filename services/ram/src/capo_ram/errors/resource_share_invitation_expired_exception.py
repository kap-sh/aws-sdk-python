"""Generated from Smithy shape ``com.amazonaws.ram#ResourceShareInvitationExpiredException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ram.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_ram.types.string


class ResourceShareInvitationExpiredException_(TypedDict, closed=True):
    message: "capo_ram.types.string.String"


# --- restJson1 ser/de ---
def serialize_json(value: ResourceShareInvitationExpiredException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ResourceShareInvitationExpiredException_:
    out: ResourceShareInvitationExpiredException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError(
            "ResourceShareInvitationExpiredException_.message required"
        )
    return out


class ResourceShareInvitationExpiredException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ram#ResourceShareInvitationExpiredException``."""

    code: str | None = "ResourceShareInvitationExpiredException"

    def __init__(self, data: ResourceShareInvitationExpiredException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceShareInvitationExpiredException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ResourceShareInvitationExpiredException":
        return cls(deserialize_json(data))

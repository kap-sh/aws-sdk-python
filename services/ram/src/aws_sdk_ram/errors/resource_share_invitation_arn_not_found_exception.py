"""Generated from Smithy shape ``com.amazonaws.ram#ResourceShareInvitationArnNotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ram.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_ram.types.string


class ResourceShareInvitationArnNotFoundException_(TypedDict, closed=True):
    message: "aws_sdk_ram.types.string.String"


# --- restJson1 ser/de ---
def serialize_json(value: ResourceShareInvitationArnNotFoundException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ResourceShareInvitationArnNotFoundException_:
    out: ResourceShareInvitationArnNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError(
            "ResourceShareInvitationArnNotFoundException_.message required"
        )
    return out


class ResourceShareInvitationArnNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ram#ResourceShareInvitationArnNotFoundException``."""

    code: str | None = "ResourceShareInvitationArnNotFoundException"

    def __init__(self, data: ResourceShareInvitationArnNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceShareInvitationArnNotFoundException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ResourceShareInvitationArnNotFoundException":
        return cls(deserialize_json(data))

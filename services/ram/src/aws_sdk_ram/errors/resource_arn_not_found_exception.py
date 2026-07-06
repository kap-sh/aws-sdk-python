"""Generated from Smithy shape ``com.amazonaws.ram#ResourceArnNotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ram.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_ram.types.string


class ResourceArnNotFoundException_(TypedDict, closed=True):
    message: "aws_sdk_ram.types.string.String"


# --- restJson1 ser/de ---
def serialize_json(value: ResourceArnNotFoundException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ResourceArnNotFoundException_:
    out: ResourceArnNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ResourceArnNotFoundException_.message required")
    return out


class ResourceArnNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ram#ResourceArnNotFoundException``."""

    code: str | None = "ResourceArnNotFoundException"

    def __init__(self, data: ResourceArnNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceArnNotFoundException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ResourceArnNotFoundException":
        return cls(deserialize_json(data))

"""Generated from Smithy shape ``com.amazonaws.ram#MalformedArnException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ram.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_ram.types.string


class MalformedArnException_(TypedDict, closed=True):
    message: "aws_sdk_ram.types.string.String"


# --- restJson1 ser/de ---
def serialize_json(value: MalformedArnException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> MalformedArnException_:
    out: MalformedArnException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("MalformedArnException_.message required")
    return out


class MalformedArnException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ram#MalformedArnException``."""

    code: str | None = "MalformedArnException"

    def __init__(self, data: MalformedArnException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="MalformedArnException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "MalformedArnException":
        return cls(deserialize_json(data))

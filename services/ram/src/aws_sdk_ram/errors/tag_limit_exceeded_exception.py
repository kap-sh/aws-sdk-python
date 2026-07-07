"""Generated from Smithy shape ``com.amazonaws.ram#TagLimitExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ram.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_ram.types.string


class TagLimitExceededException_(TypedDict, closed=True):
    message: "aws_sdk_ram.types.string.String"


# --- restJson1 ser/de ---
def serialize_json(value: TagLimitExceededException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> TagLimitExceededException_:
    out: TagLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("TagLimitExceededException_.message required")
    return out


class TagLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ram#TagLimitExceededException``."""

    code: str | None = "TagLimitExceededException"

    def __init__(self, data: TagLimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TagLimitExceededException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "TagLimitExceededException":
        return cls(deserialize_json(data))

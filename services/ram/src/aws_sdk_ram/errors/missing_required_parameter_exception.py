"""Generated from Smithy shape ``com.amazonaws.ram#MissingRequiredParameterException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ram.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_ram.types.string


class MissingRequiredParameterException_(TypedDict, closed=True):
    message: "aws_sdk_ram.types.string.String"


# --- restJson1 ser/de ---
def serialize_json(value: MissingRequiredParameterException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> MissingRequiredParameterException_:
    out: MissingRequiredParameterException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError(
            "MissingRequiredParameterException_.message required"
        )
    return out


class MissingRequiredParameterException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ram#MissingRequiredParameterException``."""

    code: str | None = "MissingRequiredParameterException"

    def __init__(self, data: MissingRequiredParameterException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="MissingRequiredParameterException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "MissingRequiredParameterException":
        return cls(deserialize_json(data))

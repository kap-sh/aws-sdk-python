"""Generated from Smithy shape ``com.amazonaws.elementalinference#InternalServerErrorException``."""

from typing_extensions import TypedDict

from aws_sdk_elementalinference.errors import DeserializationError, ServiceError


class InternalServerErrorException_(TypedDict, closed=True):
    message: "str"


# --- restJson1 ser/de ---
def serialize_json(value: InternalServerErrorException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InternalServerErrorException_:
    out: InternalServerErrorException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("InternalServerErrorException_.message required")
    return out


class InternalServerErrorException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.elementalinference#InternalServerErrorException``."""

    code: str | None = "InternalServerErrorException"

    def __init__(self, data: InternalServerErrorException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=True,
            code="InternalServerErrorException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InternalServerErrorException":
        return cls(deserialize_json(data))

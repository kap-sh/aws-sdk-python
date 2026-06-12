"""Generated from Smithy shape ``com.amazonaws.simpledbv2#InvalidParameterCombinationException``."""

from typing import TypedDict

from aws_sdk_simpledbv2.errors import DeserializationError, ServiceError


class InvalidParameterCombinationException_(TypedDict):
    message: "str"


# --- restJson1 ser/de ---
def serialize_json(value: InvalidParameterCombinationException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidParameterCombinationException_:
    out: InvalidParameterCombinationException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError(
            "InvalidParameterCombinationException_.message required"
        )
    return out


class InvalidParameterCombinationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.simpledbv2#InvalidParameterCombinationException``."""

    code: str | None = "InvalidParameterCombinationException"

    def __init__(self, data: InvalidParameterCombinationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidParameterCombinationException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidParameterCombinationException":
        return cls(deserialize_json(data))

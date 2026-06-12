"""Generated from Smithy shape ``com.amazonaws.simpledbv2#InvalidParameterValueException``."""

from typing import TypedDict

from aws_sdk_simpledbv2.errors import DeserializationError, ServiceError


class InvalidParameterValueException_(TypedDict):
    message: "str"


# --- restJson1 ser/de ---
def serialize_json(value: InvalidParameterValueException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidParameterValueException_:
    out: InvalidParameterValueException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("InvalidParameterValueException_.message required")
    return out


class InvalidParameterValueException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.simpledbv2#InvalidParameterValueException``."""

    code: str | None = "InvalidParameterValueException"

    def __init__(self, data: InvalidParameterValueException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidParameterValueException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidParameterValueException":
        return cls(deserialize_json(data))

"""Generated from Smithy shape ``com.amazonaws.securityir#InvalidTokenException``."""

from typing import TypedDict

from aws_sdk_security_ir.errors import DeserializationError, ServiceError


class InvalidTokenException_(TypedDict):
    message: "str"
    """<p>The exception message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvalidTokenException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidTokenException_:
    out: InvalidTokenException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("InvalidTokenException_.message required")
    return out


class InvalidTokenException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.securityir#InvalidTokenException``."""

    code: str | None = "InvalidTokenException"

    def __init__(self, data: InvalidTokenException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=True,
            code="InvalidTokenException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidTokenException":
        return cls(deserialize_json(data))

"""Generated from Smithy shape ``com.amazonaws.qapps#UnauthorizedException``."""

from typing_extensions import TypedDict

from aws_sdk_qapps.errors import DeserializationError, ServiceError


class UnauthorizedException_(TypedDict, closed=True):
    message: "str"


# --- restJson1 ser/de ---
def serialize_json(value: UnauthorizedException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> UnauthorizedException_:
    out: UnauthorizedException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("UnauthorizedException_.message required")
    return out


class UnauthorizedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.qapps#UnauthorizedException``."""

    code: str | None = "UnauthorizedException"

    def __init__(self, data: UnauthorizedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnauthorizedException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "UnauthorizedException":
        return cls(deserialize_json(data))

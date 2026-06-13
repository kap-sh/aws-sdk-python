"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterOutputServiceQuotaExceededException``."""

from typing import TypedDict

from aws_sdk_mediaconnect.errors import DeserializationError, ServiceError


class RouterOutputServiceQuotaExceededException_(TypedDict):
    message: "str"


# --- restJson1 ser/de ---
def serialize_json(value: RouterOutputServiceQuotaExceededException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> RouterOutputServiceQuotaExceededException_:
    out: RouterOutputServiceQuotaExceededException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError(
            "RouterOutputServiceQuotaExceededException_.message required"
        )
    return out


class RouterOutputServiceQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.mediaconnect#RouterOutputServiceQuotaExceededException``."""

    code: str | None = "RouterOutputServiceQuotaExceededException"

    def __init__(self, data: RouterOutputServiceQuotaExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="RouterOutputServiceQuotaExceededException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "RouterOutputServiceQuotaExceededException":
        return cls(deserialize_json(data))

"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterInputServiceQuotaExceededException``."""

from typing_extensions import TypedDict

from aws_sdk_mediaconnect.errors import DeserializationError, ServiceError


class RouterInputServiceQuotaExceededException_(TypedDict, closed=True):
    message: "str"


# --- restJson1 ser/de ---
def serialize_json(value: RouterInputServiceQuotaExceededException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> RouterInputServiceQuotaExceededException_:
    out: RouterInputServiceQuotaExceededException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError(
            "RouterInputServiceQuotaExceededException_.message required"
        )
    return out


class RouterInputServiceQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.mediaconnect#RouterInputServiceQuotaExceededException``."""

    code: str | None = "RouterInputServiceQuotaExceededException"

    def __init__(self, data: RouterInputServiceQuotaExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="RouterInputServiceQuotaExceededException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "RouterInputServiceQuotaExceededException":
        return cls(deserialize_json(data))

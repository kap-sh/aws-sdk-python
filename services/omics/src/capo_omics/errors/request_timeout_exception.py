"""Generated from Smithy shape ``com.amazonaws.omics#RequestTimeoutException``."""

from typing_extensions import TypedDict

from capo_omics.errors import DeserializationError, ServiceError


class RequestTimeoutException_(TypedDict, closed=True):
    message: "str"


# --- restJson1 ser/de ---
def serialize_json(value: RequestTimeoutException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> RequestTimeoutException_:
    out: RequestTimeoutException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("RequestTimeoutException_.message required")
    return out


class RequestTimeoutException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.omics#RequestTimeoutException``."""

    code: str | None = "RequestTimeoutException"

    def __init__(self, data: RequestTimeoutException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="RequestTimeoutException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "RequestTimeoutException":
        return cls(deserialize_json(data))

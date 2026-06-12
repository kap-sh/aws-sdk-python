"""Generated from Smithy shape ``com.amazonaws.account#ResourceUnavailableException``."""

from typing import TypedDict

from typing_extensions import NotRequired

from aws_sdk_account.errors import DeserializationError, ServiceError


class ResourceUnavailableException_(TypedDict):
    message: "str"
    error_type: NotRequired["str"]
    """<p>The value populated to the <code>x-amzn-ErrorType</code> response header by API Gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceUnavailableException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ResourceUnavailableException_:
    out: ResourceUnavailableException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ResourceUnavailableException_.message required")
    return out


class ResourceUnavailableException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.account#ResourceUnavailableException``."""

    code: str | None = "ResourceUnavailableException"

    def __init__(self, data: ResourceUnavailableException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceUnavailableException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ResourceUnavailableException":
        return cls(deserialize_json(data))

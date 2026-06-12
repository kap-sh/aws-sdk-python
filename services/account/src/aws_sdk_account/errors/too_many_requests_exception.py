"""Generated from Smithy shape ``com.amazonaws.account#TooManyRequestsException``."""

from typing import TypedDict

from typing_extensions import NotRequired

from aws_sdk_account.errors import DeserializationError, ServiceError


class TooManyRequestsException_(TypedDict):
    message: "str"
    error_type: NotRequired["str"]
    """<p>The value populated to the <code>x-amzn-ErrorType</code> response header by API Gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TooManyRequestsException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> TooManyRequestsException_:
    out: TooManyRequestsException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("TooManyRequestsException_.message required")
    return out


class TooManyRequestsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.account#TooManyRequestsException``."""

    code: str | None = "TooManyRequestsException"

    def __init__(self, data: TooManyRequestsException_):
        super().__init__(
            "client",
            is_throttling_error=True,
            is_retryable=True,
            code="TooManyRequestsException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "TooManyRequestsException":
        return cls(deserialize_json(data))

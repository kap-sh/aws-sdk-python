"""Generated from Smithy shape ``com.amazonaws.cognitosync#LambdaThrottledException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cognito_sync.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_cognito_sync.types.exception_message


class LambdaThrottledException_(TypedDict, closed=True):
    message: "capo_cognito_sync.types.exception_message.ExceptionMessage"
    """<p>A message returned when an LambdaThrottledException is thrown</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LambdaThrottledException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> LambdaThrottledException_:
    out: LambdaThrottledException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("LambdaThrottledException_.message required")
    return out


class LambdaThrottledException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cognitosync#LambdaThrottledException``."""

    code: str | None = "LambdaThrottledException"

    def __init__(self, data: LambdaThrottledException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="LambdaThrottledException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "LambdaThrottledException":
        return cls(deserialize_json(data))

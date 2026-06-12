"""Generated from Smithy shape ``com.amazonaws.cognitosync#ConcurrentModificationException``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cognito_sync.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_cognito_sync.types.string


class ConcurrentModificationException_(TypedDict):
    message: "aws_sdk_cognito_sync.types.string.String"
    """<p>The message returned by a ConcurrentModicationException.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConcurrentModificationException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ConcurrentModificationException_:
    out: ConcurrentModificationException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ConcurrentModificationException_.message required")
    return out


class ConcurrentModificationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cognitosync#ConcurrentModificationException``."""

    code: str | None = "ConcurrentModificationException"

    def __init__(self, data: ConcurrentModificationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConcurrentModificationException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ConcurrentModificationException":
        return cls(deserialize_json(data))

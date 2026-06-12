"""Generated from Smithy shape ``com.amazonaws.codeartifact#ThrottlingException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codeartifact.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.retry_after_seconds
    import aws_sdk_codeartifact.types.string


class ThrottlingException_(TypedDict):
    message: "aws_sdk_codeartifact.types.string.String"
    retry_after_seconds: NotRequired[
        "aws_sdk_codeartifact.types.retry_after_seconds.RetryAfterSeconds"
    ]
    """<p> The time period, in seconds, to wait before retrying the request. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThrottlingException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ThrottlingException_:
    out: ThrottlingException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ThrottlingException_.message required")
    return out


class ThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codeartifact#ThrottlingException``."""

    code: str | None = "ThrottlingException"

    def __init__(self, data: ThrottlingException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ThrottlingException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ThrottlingException":
        return cls(deserialize_json(data))

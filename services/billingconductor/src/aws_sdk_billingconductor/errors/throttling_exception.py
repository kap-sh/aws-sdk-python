"""Generated from Smithy shape ``com.amazonaws.billingconductor#ThrottlingException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_billingconductor.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.retry_after_seconds
    import aws_sdk_billingconductor.types.string


class ThrottlingException_(TypedDict, closed=True):
    message: "aws_sdk_billingconductor.types.string.String"
    retry_after_seconds: (
        "aws_sdk_billingconductor.types.retry_after_seconds.RetryAfterSeconds"
    )
    """<p>Number of seconds you can safely retry after the call. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThrottlingException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ThrottlingException_:
    out: ThrottlingException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("ThrottlingException_.message required")
    return out


class ThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.billingconductor#ThrottlingException``."""

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

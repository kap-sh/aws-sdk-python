"""Generated from Smithy shape ``com.amazonaws.migrationhubconfig#ThrottlingException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_migrationhub_config.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_migrationhub_config.types.error_message
    import aws_sdk_migrationhub_config.types.retry_after_seconds


class ThrottlingException_(TypedDict, closed=True):
    message: "aws_sdk_migrationhub_config.types.error_message.ErrorMessage"
    retry_after_seconds: (
        "aws_sdk_migrationhub_config.types.retry_after_seconds.RetryAfterSeconds"
    )
    """<p>The number of seconds the caller should wait before retrying.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ThrottlingException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ThrottlingException_:
    out: ThrottlingException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("ThrottlingException_.message required")
    return out


class ThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.migrationhubconfig#ThrottlingException``."""

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
    def from_aws_json_1_1(cls, data: dict) -> "ThrottlingException":
        return cls(deserialize_aws_json_1_1(data))

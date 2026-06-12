"""Generated from Smithy shape ``com.amazonaws.migrationhub#ThrottlingException``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_migration_hub.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_migration_hub.types.error_message
    import aws_sdk_migration_hub.types.retry_after_seconds


class ThrottlingException_(TypedDict):
    message: "aws_sdk_migration_hub.types.error_message.ErrorMessage"
    """<p>A message that provides information about the exception.</p>"""
    retry_after_seconds: (
        "aws_sdk_migration_hub.types.retry_after_seconds.RetryAfterSeconds"
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
    """Modeled error for Smithy shape ``com.amazonaws.migrationhub#ThrottlingException``."""

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

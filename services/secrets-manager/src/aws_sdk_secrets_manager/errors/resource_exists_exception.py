"""Generated from Smithy shape ``com.amazonaws.secretsmanager#ResourceExistsException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_secrets_manager.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.error_message


class ResourceExistsException_(TypedDict):
    message: NotRequired["aws_sdk_secrets_manager.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceExistsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceExistsException_:
    out: ResourceExistsException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ResourceExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.secretsmanager#ResourceExistsException``."""

    code: str | None = "ResourceExistsException"

    def __init__(self, data: ResourceExistsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceExistsException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ResourceExistsException":
        return cls(deserialize_aws_json_1_1(data))

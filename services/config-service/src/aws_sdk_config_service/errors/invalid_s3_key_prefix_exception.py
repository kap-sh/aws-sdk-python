"""Generated from Smithy shape ``com.amazonaws.configservice#InvalidS3KeyPrefixException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_config_service.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.error_message


class InvalidS3KeyPrefixException_(TypedDict):
    message: NotRequired["aws_sdk_config_service.types.error_message.ErrorMessage"]
    """<p>Error executing the command</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidS3KeyPrefixException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidS3KeyPrefixException_:
    out: InvalidS3KeyPrefixException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidS3KeyPrefixException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.configservice#InvalidS3KeyPrefixException``."""

    code: str | None = "InvalidS3KeyPrefixException"

    def __init__(self, data: InvalidS3KeyPrefixException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidS3KeyPrefixException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidS3KeyPrefixException":
        return cls(deserialize_aws_json_1_1(data))

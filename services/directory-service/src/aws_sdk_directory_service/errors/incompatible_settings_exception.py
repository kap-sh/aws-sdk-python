"""Generated from Smithy shape ``com.amazonaws.directoryservice#IncompatibleSettingsException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_directory_service.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.exception_message
    import aws_sdk_directory_service.types.request_id


class IncompatibleSettingsException_(TypedDict):
    message: NotRequired[
        "aws_sdk_directory_service.types.exception_message.ExceptionMessage"
    ]
    request_id: NotRequired["aws_sdk_directory_service.types.request_id.RequestId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IncompatibleSettingsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IncompatibleSettingsException_:
    out: IncompatibleSettingsException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out


class IncompatibleSettingsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.directoryservice#IncompatibleSettingsException``."""

    code: str | None = "IncompatibleSettingsException"

    def __init__(self, data: IncompatibleSettingsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="IncompatibleSettingsException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "IncompatibleSettingsException":
        return cls(deserialize_aws_json_1_1(data))

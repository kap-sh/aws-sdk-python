"""Generated from Smithy shape ``com.amazonaws.configservice#NoRunningConfigurationRecorderException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_config_service.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.error_message


class NoRunningConfigurationRecorderException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_config_service.types.error_message.ErrorMessage"]
    """<p>Error executing the command</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NoRunningConfigurationRecorderException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NoRunningConfigurationRecorderException_:
    out: NoRunningConfigurationRecorderException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class NoRunningConfigurationRecorderException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.configservice#NoRunningConfigurationRecorderException``."""

    code: str | None = "NoRunningConfigurationRecorderException"

    def __init__(self, data: NoRunningConfigurationRecorderException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NoRunningConfigurationRecorderException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "NoRunningConfigurationRecorderException":
        return cls(deserialize_aws_json_1_1(data))

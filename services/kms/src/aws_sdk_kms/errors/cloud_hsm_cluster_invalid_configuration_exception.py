"""Generated from Smithy shape ``com.amazonaws.kms#CloudHsmClusterInvalidConfigurationException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_kms.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_kms.types.error_message_type


class CloudHsmClusterInvalidConfigurationException_(TypedDict):
    message: NotRequired["aws_sdk_kms.types.error_message_type.ErrorMessageType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: CloudHsmClusterInvalidConfigurationException_,
) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> CloudHsmClusterInvalidConfigurationException_:
    out: CloudHsmClusterInvalidConfigurationException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class CloudHsmClusterInvalidConfigurationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kms#CloudHsmClusterInvalidConfigurationException``."""

    code: str | None = "CloudHsmClusterInvalidConfigurationException"

    def __init__(self, data: CloudHsmClusterInvalidConfigurationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CloudHsmClusterInvalidConfigurationException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict
    ) -> "CloudHsmClusterInvalidConfigurationException":
        return cls(deserialize_aws_json_1_1(data))

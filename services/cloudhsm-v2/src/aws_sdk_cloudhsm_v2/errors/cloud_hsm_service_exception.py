"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#CloudHsmServiceException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudhsm_v2.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudhsm_v2.types.error_message


class CloudHsmServiceException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_cloudhsm_v2.types.error_message.errorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloudHsmServiceException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CloudHsmServiceException_:
    out: CloudHsmServiceException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class CloudHsmServiceException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudhsmv2#CloudHsmServiceException``."""

    code: str | None = "CloudHsmServiceException"

    def __init__(self, data: CloudHsmServiceException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CloudHsmServiceException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "CloudHsmServiceException":
        return cls(deserialize_aws_json_1_1(data))

"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#CloudHsmResourceLimitExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudhsm_v2.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudhsm_v2.types.error_message


class CloudHsmResourceLimitExceededException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_cloudhsm_v2.types.error_message.errorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloudHsmResourceLimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CloudHsmResourceLimitExceededException_:
    out: CloudHsmResourceLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class CloudHsmResourceLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudhsmv2#CloudHsmResourceLimitExceededException``."""

    code: str | None = "CloudHsmResourceLimitExceededException"

    def __init__(self, data: CloudHsmResourceLimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CloudHsmResourceLimitExceededException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "CloudHsmResourceLimitExceededException":
        return cls(deserialize_aws_json_1_1(data))

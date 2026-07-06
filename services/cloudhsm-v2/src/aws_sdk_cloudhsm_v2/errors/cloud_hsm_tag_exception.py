"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#CloudHsmTagException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudhsm_v2.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudhsm_v2.types.error_message


class CloudHsmTagException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_cloudhsm_v2.types.error_message.errorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloudHsmTagException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CloudHsmTagException_:
    out: CloudHsmTagException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class CloudHsmTagException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudhsmv2#CloudHsmTagException``."""

    code: str | None = "CloudHsmTagException"

    def __init__(self, data: CloudHsmTagException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CloudHsmTagException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "CloudHsmTagException":
        return cls(deserialize_aws_json_1_1(data))

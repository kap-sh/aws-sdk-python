"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#CloudHsmResourceNotFoundException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudhsm_v2.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudhsm_v2.types.error_message


class CloudHsmResourceNotFoundException_(TypedDict):
    message: NotRequired["aws_sdk_cloudhsm_v2.types.error_message.errorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloudHsmResourceNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CloudHsmResourceNotFoundException_:
    out: CloudHsmResourceNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class CloudHsmResourceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudhsmv2#CloudHsmResourceNotFoundException``."""

    code: str | None = "CloudHsmResourceNotFoundException"

    def __init__(self, data: CloudHsmResourceNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CloudHsmResourceNotFoundException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "CloudHsmResourceNotFoundException":
        return cls(deserialize_aws_json_1_1(data))

"""Generated from Smithy shape ``com.amazonaws.cloudcontrol#ServiceInternalErrorException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudcontrol.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudcontrol.types.error_message


class ServiceInternalErrorException_(TypedDict):
    message: NotRequired["aws_sdk_cloudcontrol.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ServiceInternalErrorException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ServiceInternalErrorException_:
    out: ServiceInternalErrorException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ServiceInternalErrorException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudcontrol#ServiceInternalErrorException``."""

    code: str | None = "ServiceInternalErrorException"

    def __init__(self, data: ServiceInternalErrorException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceInternalErrorException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "ServiceInternalErrorException":
        return cls(deserialize_aws_json_1_0(data))

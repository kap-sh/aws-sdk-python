"""Generated from Smithy shape ``com.amazonaws.cloudcontrol#NetworkFailureException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudcontrol.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudcontrol.types.error_message


class NetworkFailureException_(TypedDict):
    message: NotRequired["aws_sdk_cloudcontrol.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NetworkFailureException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> NetworkFailureException_:
    out: NetworkFailureException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class NetworkFailureException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudcontrol#NetworkFailureException``."""

    code: str | None = "NetworkFailureException"

    def __init__(self, data: NetworkFailureException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="NetworkFailureException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "NetworkFailureException":
        return cls(deserialize_aws_json_1_0(data))

"""Generated from Smithy shape ``com.amazonaws.cloudcontrol#HandlerInternalFailureException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudcontrol.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudcontrol.types.error_message


class HandlerInternalFailureException_(TypedDict):
    message: NotRequired["aws_sdk_cloudcontrol.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: HandlerInternalFailureException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> HandlerInternalFailureException_:
    out: HandlerInternalFailureException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class HandlerInternalFailureException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudcontrol#HandlerInternalFailureException``."""

    code: str | None = "HandlerInternalFailureException"

    def __init__(self, data: HandlerInternalFailureException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="HandlerInternalFailureException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "HandlerInternalFailureException":
        return cls(deserialize_aws_json_1_0(data))

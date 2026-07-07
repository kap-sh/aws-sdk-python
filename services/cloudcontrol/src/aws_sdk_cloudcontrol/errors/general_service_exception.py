"""Generated from Smithy shape ``com.amazonaws.cloudcontrol#GeneralServiceException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudcontrol.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudcontrol.types.error_message


class GeneralServiceException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_cloudcontrol.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GeneralServiceException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GeneralServiceException_:
    out: GeneralServiceException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class GeneralServiceException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudcontrol#GeneralServiceException``."""

    code: str | None = "GeneralServiceException"

    def __init__(self, data: GeneralServiceException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="GeneralServiceException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "GeneralServiceException":
        return cls(deserialize_aws_json_1_0(data))

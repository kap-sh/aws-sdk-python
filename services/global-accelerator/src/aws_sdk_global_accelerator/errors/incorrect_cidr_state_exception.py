"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#IncorrectCidrStateException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_global_accelerator.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.error_message


class IncorrectCidrStateException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_global_accelerator.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IncorrectCidrStateException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IncorrectCidrStateException_:
    out: IncorrectCidrStateException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class IncorrectCidrStateException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.globalaccelerator#IncorrectCidrStateException``."""

    code: str | None = "IncorrectCidrStateException"

    def __init__(self, data: IncorrectCidrStateException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="IncorrectCidrStateException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "IncorrectCidrStateException":
        return cls(deserialize_aws_json_1_1(data))

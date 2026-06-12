"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#AssociatedListenerFoundException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_global_accelerator.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.error_message


class AssociatedListenerFoundException_(TypedDict):
    message: NotRequired["aws_sdk_global_accelerator.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociatedListenerFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociatedListenerFoundException_:
    out: AssociatedListenerFoundException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class AssociatedListenerFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.globalaccelerator#AssociatedListenerFoundException``."""

    code: str | None = "AssociatedListenerFoundException"

    def __init__(self, data: AssociatedListenerFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AssociatedListenerFoundException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "AssociatedListenerFoundException":
        return cls(deserialize_aws_json_1_1(data))

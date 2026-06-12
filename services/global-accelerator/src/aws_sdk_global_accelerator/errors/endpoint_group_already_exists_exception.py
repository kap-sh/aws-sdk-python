"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#EndpointGroupAlreadyExistsException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_global_accelerator.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.error_message


class EndpointGroupAlreadyExistsException_(TypedDict):
    message: NotRequired["aws_sdk_global_accelerator.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EndpointGroupAlreadyExistsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EndpointGroupAlreadyExistsException_:
    out: EndpointGroupAlreadyExistsException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class EndpointGroupAlreadyExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.globalaccelerator#EndpointGroupAlreadyExistsException``."""

    code: str | None = "EndpointGroupAlreadyExistsException"

    def __init__(self, data: EndpointGroupAlreadyExistsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="EndpointGroupAlreadyExistsException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "EndpointGroupAlreadyExistsException":
        return cls(deserialize_aws_json_1_1(data))

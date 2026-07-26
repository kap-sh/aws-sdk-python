"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#EndpointAlreadyExistsException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_global_accelerator.errors import ServiceError

if TYPE_CHECKING:
    import capo_global_accelerator.types.error_message


class EndpointAlreadyExistsException_(TypedDict, closed=True):
    message: NotRequired["capo_global_accelerator.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EndpointAlreadyExistsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EndpointAlreadyExistsException_:
    out: EndpointAlreadyExistsException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class EndpointAlreadyExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.globalaccelerator#EndpointAlreadyExistsException``."""

    code: str | None = "EndpointAlreadyExistsException"

    def __init__(self, data: EndpointAlreadyExistsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="EndpointAlreadyExistsException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "EndpointAlreadyExistsException":
        return cls(deserialize_aws_json_1_1(data))

"""Generated from Smithy shape ``com.amazonaws.servicediscovery#InvalidInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_servicediscovery.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_servicediscovery.types.error_message


class InvalidInput_(TypedDict):
    message: NotRequired["aws_sdk_servicediscovery.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidInput_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidInput_:
    out: InvalidInput_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InvalidInput(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.servicediscovery#InvalidInput``."""

    code: str | None = "InvalidInput"

    def __init__(self, data: InvalidInput_):
        super().__init__(
            "client", is_throttling_error=False, is_retryable=False, code="InvalidInput"
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidInput":
        return cls(deserialize_aws_json_1_1(data))

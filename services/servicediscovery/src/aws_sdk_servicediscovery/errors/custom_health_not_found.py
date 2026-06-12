"""Generated from Smithy shape ``com.amazonaws.servicediscovery#CustomHealthNotFound``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_servicediscovery.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_servicediscovery.types.error_message


class CustomHealthNotFound_(TypedDict):
    message: NotRequired["aws_sdk_servicediscovery.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomHealthNotFound_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomHealthNotFound_:
    out: CustomHealthNotFound_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class CustomHealthNotFound(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.servicediscovery#CustomHealthNotFound``."""

    code: str | None = "CustomHealthNotFound"

    def __init__(self, data: CustomHealthNotFound_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CustomHealthNotFound",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "CustomHealthNotFound":
        return cls(deserialize_aws_json_1_1(data))

"""Generated from Smithy shape ``com.amazonaws.appstream#ResourceNotAvailableException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_appstream.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_appstream.types.error_message


class ResourceNotAvailableException_(TypedDict):
    message: NotRequired["aws_sdk_appstream.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceNotAvailableException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceNotAvailableException_:
    out: ResourceNotAvailableException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ResourceNotAvailableException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.appstream#ResourceNotAvailableException``."""

    code: str | None = "ResourceNotAvailableException"

    def __init__(self, data: ResourceNotAvailableException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceNotAvailableException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ResourceNotAvailableException":
        return cls(deserialize_aws_json_1_1(data))

"""Generated from Smithy shape ``com.amazonaws.mediastore#ContainerInUseException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mediastore.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_mediastore.types.error_message


class ContainerInUseException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_mediastore.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerInUseException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ContainerInUseException_:
    out: ContainerInUseException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ContainerInUseException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.mediastore#ContainerInUseException``."""

    code: str | None = "ContainerInUseException"

    def __init__(self, data: ContainerInUseException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ContainerInUseException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ContainerInUseException":
        return cls(deserialize_aws_json_1_1(data))

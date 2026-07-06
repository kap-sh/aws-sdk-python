"""Generated from Smithy shape ``com.amazonaws.kendra#ResourceAlreadyExistException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_kendra.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.error_message


class ResourceAlreadyExistException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_kendra.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceAlreadyExistException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceAlreadyExistException_:
    out: ResourceAlreadyExistException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ResourceAlreadyExistException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kendra#ResourceAlreadyExistException``."""

    code: str | None = "ResourceAlreadyExistException"

    def __init__(self, data: ResourceAlreadyExistException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceAlreadyExistException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ResourceAlreadyExistException":
        return cls(deserialize_aws_json_1_1(data))

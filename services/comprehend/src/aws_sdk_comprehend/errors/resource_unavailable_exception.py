"""Generated from Smithy shape ``com.amazonaws.comprehend#ResourceUnavailableException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_comprehend.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.string


class ResourceUnavailableException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_comprehend.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceUnavailableException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceUnavailableException_:
    out: ResourceUnavailableException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ResourceUnavailableException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.comprehend#ResourceUnavailableException``."""

    code: str | None = "ResourceUnavailableException"

    def __init__(self, data: ResourceUnavailableException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceUnavailableException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ResourceUnavailableException":
        return cls(deserialize_aws_json_1_1(data))

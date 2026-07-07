"""Generated from Smithy shape ``com.amazonaws.applicationinsights#BadRequestException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_application_insights.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_application_insights.types.error_msg


class BadRequestException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_application_insights.types.error_msg.ErrorMsg"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BadRequestException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BadRequestException_:
    out: BadRequestException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class BadRequestException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.applicationinsights#BadRequestException``."""

    code: str | None = "BadRequestException"

    def __init__(self, data: BadRequestException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="BadRequestException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "BadRequestException":
        return cls(deserialize_aws_json_1_1(data))
